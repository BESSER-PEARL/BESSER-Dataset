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
NumberingStyle: Enumeration = Enumeration(
    name="NumberingStyle",
    literals={
            EnumerationLiteral(name="ARABIC"),
			EnumerationLiteral(name="ROMAN"),
			EnumerationLiteral(name="LATIN")
    }
)

RuleResult: Enumeration = Enumeration(
    name="RuleResult",
    literals={
            EnumerationLiteral(name="ACCEPT"),
			EnumerationLiteral(name="REJECT")
    }
)

# Classes
doc_Test = Class(name="doc::Test")
doc_map_Map = Class(name="doc::map::Map")
MapContainer = Class(name="MapContainer")
NameRule = Class(name="NameRule")
doc_map_NameRule = Class(name="doc::map::NameRule", is_abstract=True)
ExtensionMappingEntry = Class(name="ExtensionMappingEntry")
doc_map_Import = Class(name="doc::map::Import", is_abstract=True)
MapElement = Class(name="MapElement")
doc_map_File = Class(name="doc::map::File")
Import = Class(name="Import")
doc_map_MapSection = Class(name="doc::map::MapSection")
map_MapContainer = Class(name="map::MapContainer")
map_MapElement = Class(name="map::MapElement")
doc_map_MapElement = Class(name="doc::map::MapElement", is_abstract=True)
doc_map_Feature = Class(name="doc::map::Feature")
doc_map_ResourceFactory = Class(name="doc::map::ResourceFactory")
doc_map_ExtensionMappingEntry = Class(name="doc::map::ExtensionMappingEntry")
ResourceFactory = Class(name="ResourceFactory")
doc_map_ContentGenerator = Class(name="doc::map::ContentGenerator", is_abstract=True)
fragment_Content = Class(name="fragment::Content")
doc_map_PatternRule = Class(name="doc::map::PatternRule", is_abstract=True)
doc_map_IncludePatternRule = Class(name="doc::map::IncludePatternRule")
PatternRule = Class(name="PatternRule")
doc_map_ExcludePatternRule = Class(name="doc::map::ExcludePatternRule")
Content = Class(name="Content")
doc_map_MapContainer = Class(name="doc::map::MapContainer", is_abstract=True)
doc_fragment_Fragment = Class(name="doc::fragment::Fragment")
Container = Class(name="Container")
doc_fragment_Section = Class(name="doc::fragment::Section", is_abstract=True)
doc_fragment_Container = Class(name="doc::fragment::Container", is_abstract=True)
doc_fragment_Copyright = Class(name="doc::fragment::Copyright")
Author = Class(name="Author")
doc_book_Book = Class(name="doc::book::Book")
BookContainer = Class(name="BookContainer")
Section = Class(name="Section")
doc_fragment_PlainTextContent = Class(name="doc::fragment::PlainTextContent")
doc_fragment_Content = Class(name="doc::fragment::Content", is_abstract=True)
doc_fragment_Author = Class(name="doc::fragment::Author")
doc_book_BookContainer = Class(name="doc::book::BookContainer", is_abstract=True)
BookSection = Class(name="BookSection")
Copyright = Class(name="Copyright")
doc_book_BookSection = Class(name="doc::book::BookSection")
doc_builder_BookBuilder = Class(name="doc::builder::BookBuilder")
Map = Class(name="Map")
builder_PropertyEntry = Class(name="builder::PropertyEntry")
doc_builder_PropertyEntry = Class(name="doc::builder::PropertyEntry")

# doc_Test class attributes and methods

# doc_map_Map class attributes and methods
doc_map_Map_m_visit: Method = Method(name="visit", parameters={Parameter(name='visitor')})
doc_map_Map.methods={doc_map_Map_m_visit}

# MapContainer class attributes and methods

# NameRule class attributes and methods

# doc_map_NameRule class attributes and methods
doc_map_NameRule_m_checkRule: Method = Method(name="checkRule", parameters={Parameter(name='name')}, type=StringType)
doc_map_NameRule.methods={doc_map_NameRule_m_checkRule}

# ExtensionMappingEntry class attributes and methods

# doc_map_Import class attributes and methods

# MapElement class attributes and methods

# doc_map_File class attributes and methods
doc_map_File_path: Property = Property(name="path", type=StringType)
doc_map_File.attributes={doc_map_File_path}

# Import class attributes and methods

# doc_map_MapSection class attributes and methods
doc_map_MapSection_title: Property = Property(name="title", type=StringType)
doc_map_MapSection_id: Property = Property(name="id", type=StringType)
doc_map_MapSection.attributes={doc_map_MapSection_id, doc_map_MapSection_title}

# map_MapContainer class attributes and methods

# map_MapElement class attributes and methods

# doc_map_MapElement class attributes and methods
doc_map_MapElement_m_visit: Method = Method(name="visit", parameters={Parameter(name='visitor')})
doc_map_MapElement.methods={doc_map_MapElement_m_visit}

# doc_map_Feature class attributes and methods
doc_map_Feature_featureId: Property = Property(name="featureId", type=StringType)
doc_map_Feature_createSection: Property = Property(name="createSection", type=BooleanType)
doc_map_Feature.attributes={doc_map_Feature_createSection, doc_map_Feature_featureId}

# doc_map_ResourceFactory class attributes and methods
doc_map_ResourceFactory_className: Property = Property(name="className", type=StringType)
doc_map_ResourceFactory.attributes={doc_map_ResourceFactory_className}

# doc_map_ExtensionMappingEntry class attributes and methods
doc_map_ExtensionMappingEntry_extension: Property = Property(name="extension", type=StringType)
doc_map_ExtensionMappingEntry.attributes={doc_map_ExtensionMappingEntry_extension}

# ResourceFactory class attributes and methods

# doc_map_ContentGenerator class attributes and methods

# fragment_Content class attributes and methods

# doc_map_PatternRule class attributes and methods
doc_map_PatternRule_pattern: Property = Property(name="pattern", type=StringType)
doc_map_PatternRule.attributes={doc_map_PatternRule_pattern}

# doc_map_IncludePatternRule class attributes and methods
doc_map_IncludePatternRule_m_checkRule: Method = Method(name="checkRule", parameters={Parameter(name='name')}, type=StringType)
doc_map_IncludePatternRule.methods={doc_map_IncludePatternRule_m_checkRule}

# PatternRule class attributes and methods

# doc_map_ExcludePatternRule class attributes and methods
doc_map_ExcludePatternRule_m_checkRule: Method = Method(name="checkRule", parameters={Parameter(name='name')}, type=StringType)
doc_map_ExcludePatternRule.methods={doc_map_ExcludePatternRule_m_checkRule}

# Content class attributes and methods

# doc_map_MapContainer class attributes and methods
doc_map_MapContainer_numberingStyle: Property = Property(name="numberingStyle", type=StringType)
doc_map_MapContainer.attributes={doc_map_MapContainer_numberingStyle}

# doc_fragment_Fragment class attributes and methods

# Container class attributes and methods

# doc_fragment_Section class attributes and methods
doc_fragment_Section_title: Property = Property(name="title", type=StringType)
doc_fragment_Section.attributes={doc_fragment_Section_title}

# doc_fragment_Container class attributes and methods
doc_fragment_Container_content: Property = Property(name="content", type=StringType)
doc_fragment_Container.attributes={doc_fragment_Container_content}

# doc_fragment_Copyright class attributes and methods
doc_fragment_Copyright_year: Property = Property(name="year", type=IntegerType)
doc_fragment_Copyright.attributes={doc_fragment_Copyright_year}

# Author class attributes and methods

# doc_book_Book class attributes and methods
doc_book_Book_title: Property = Property(name="title", type=StringType)
doc_book_Book_version: Property = Property(name="version", type=StringType)
doc_book_Book_copyrightMarker: Property = Property(name="copyrightMarker", type=StringType)
doc_book_Book_copyrightText: Property = Property(name="copyrightText", type=StringType)
doc_book_Book.attributes={doc_book_Book_version, doc_book_Book_copyrightMarker, doc_book_Book_title, doc_book_Book_copyrightText}

# BookContainer class attributes and methods

# Section class attributes and methods

# doc_fragment_PlainTextContent class attributes and methods
doc_fragment_PlainTextContent_value: Property = Property(name="value", type=StringType)
doc_fragment_PlainTextContent.attributes={doc_fragment_PlainTextContent_value}

# doc_fragment_Content class attributes and methods

# doc_fragment_Author class attributes and methods
doc_fragment_Author_ref: Property = Property(name="ref", type=StringType)
doc_fragment_Author_id: Property = Property(name="id", type=StringType)
doc_fragment_Author_name: Property = Property(name="name", type=StringType)
doc_fragment_Author.attributes={doc_fragment_Author_id, doc_fragment_Author_name, doc_fragment_Author_ref}

# doc_book_BookContainer class attributes and methods
doc_book_BookContainer_numberingStyle: Property = Property(name="numberingStyle", type=StringType)
doc_book_BookContainer.attributes={doc_book_BookContainer_numberingStyle}

# BookSection class attributes and methods

# Copyright class attributes and methods

# doc_book_BookSection class attributes and methods
doc_book_BookSection_id: Property = Property(name="id", type=StringType)
doc_book_BookSection_number: Property = Property(name="number", type=IntegerType)
doc_book_BookSection_fullNumber: Property = Property(name="fullNumber", type=StringType)
doc_book_BookSection_title: Property = Property(name="title", type=StringType)
doc_book_BookSection.attributes={doc_book_BookSection_number, doc_book_BookSection_title, doc_book_BookSection_id, doc_book_BookSection_fullNumber}

# doc_builder_BookBuilder class attributes and methods
doc_builder_BookBuilder_title: Property = Property(name="title", type=StringType)
doc_builder_BookBuilder_version: Property = Property(name="version", type=StringType)
doc_builder_BookBuilder_license: Property = Property(name="license", type=StringType)
doc_builder_BookBuilder_copyrightMarker: Property = Property(name="copyrightMarker", type=StringType)
doc_builder_BookBuilder.attributes={doc_builder_BookBuilder_copyrightMarker, doc_builder_BookBuilder_license, doc_builder_BookBuilder_title, doc_builder_BookBuilder_version}

# Map class attributes and methods

# builder_PropertyEntry class attributes and methods

# doc_builder_PropertyEntry class attributes and methods
doc_builder_PropertyEntry_key: Property = Property(name="key", type=StringType)
doc_builder_PropertyEntry_value: Property = Property(name="value", type=StringType)
doc_builder_PropertyEntry.attributes={doc_builder_PropertyEntry_key, doc_builder_PropertyEntry_value}

# Relationships
fileNameRules1: BinaryAssociation = BinaryAssociation(
    name="fileNameRules1",
    ends={
        Property(name="NameRule", type=doc_map_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_map_Feature", type=NameRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionMappings0: BinaryAssociation = BinaryAssociation(
    name="extensionMappings0",
    ends={
        Property(name="ExtensionMappingEntry", type=doc_map_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_map_Map", type=ExtensionMappingEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factory2: BinaryAssociation = BinaryAssociation(
    name="factory2",
    ends={
        Property(name="ResourceFactory", type=doc_map_ExtensionMappingEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_map_ExtensionMappingEntry", type=ResourceFactory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anyContent4: BinaryAssociation = BinaryAssociation(
    name="anyContent4",
    ends={
        Property(name="Content", type=doc_fragment_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_fragment_Container", type=Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="MapElement", type=doc_map_MapContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_map_MapContainer", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author7: BinaryAssociation = BinaryAssociation(
    name="author7",
    ends={
        Property(name="Author", type=doc_fragment_Copyright, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_fragment_Copyright", type=Author, multiplicity=Multiplicity(1, 9999))
    }
)
section5: BinaryAssociation = BinaryAssociation(
    name="section5",
    ends={
        Property(name="Section", type=doc_fragment_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_fragment_Container6", type=Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content12: BinaryAssociation = BinaryAssociation(
    name="content12",
    ends={
        Property(name="Content13", type=doc_book_BookContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_book_BookContainer", type=Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections14: BinaryAssociation = BinaryAssociation(
    name="sections14",
    ends={
        Property(name="BookSection", type=doc_book_BookContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_book_BookContainer15", type=BookSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors8: BinaryAssociation = BinaryAssociation(
    name="authors8",
    ends={
        Property(name="Author9", type=doc_book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_book_Book", type=Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
copyright10: BinaryAssociation = BinaryAssociation(
    name="copyright10",
    ends={
        Property(name="Copyright", type=doc_book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_book_Book11", type=Copyright, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors16: BinaryAssociation = BinaryAssociation(
    name="authors16",
    ends={
        Property(name="Author17", type=doc_builder_BookBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_builder_BookBuilder", type=Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
copyright18: BinaryAssociation = BinaryAssociation(
    name="copyright18",
    ends={
        Property(name="Copyright20", type=doc_builder_BookBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_builder_BookBuilder19", type=Copyright, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties21: BinaryAssociation = BinaryAssociation(
    name="properties21",
    ends={
        Property(name="builder_PropertyEntry", type=doc_builder_BookBuilder, multiplicity=Multiplicity(1, 1)),
        Property(name="doc_builder_BookBuilder22", type=builder_PropertyEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_doc_map_Map_MapContainer = Generalization(general=MapContainer, specific=doc_map_Map)
gen_doc_map_Feature_Import = Generalization(general=Import, specific=doc_map_Feature)
gen_doc_map_Import_MapElement = Generalization(general=MapElement, specific=doc_map_Import)
gen_doc_map_File_Import = Generalization(general=Import, specific=doc_map_File)
gen_doc_map_MapSection_map_MapContainer = Generalization(general=map_MapContainer, specific=doc_map_MapSection)
gen_doc_map_MapSection_map_MapElement = Generalization(general=map_MapElement, specific=doc_map_MapSection)
gen_doc_map_ContentGenerator_map_MapElement = Generalization(general=map_MapElement, specific=doc_map_ContentGenerator)
gen_doc_map_ContentGenerator_fragment_Content = Generalization(general=fragment_Content, specific=doc_map_ContentGenerator)
gen_doc_map_PatternRule_NameRule = Generalization(general=NameRule, specific=doc_map_PatternRule)
gen_doc_map_IncludePatternRule_PatternRule = Generalization(general=PatternRule, specific=doc_map_IncludePatternRule)
gen_doc_map_ExcludePatternRule_PatternRule = Generalization(general=PatternRule, specific=doc_map_ExcludePatternRule)
gen_doc_fragment_Fragment_Container = Generalization(general=Container, specific=doc_fragment_Fragment)
gen_doc_fragment_Section_Container = Generalization(general=Container, specific=doc_fragment_Section)
gen_doc_book_Book_BookContainer = Generalization(general=BookContainer, specific=doc_book_Book)
gen_doc_fragment_PlainTextContent_Content = Generalization(general=Content, specific=doc_fragment_PlainTextContent)
gen_doc_book_BookSection_BookContainer = Generalization(general=BookContainer, specific=doc_book_BookSection)
gen_doc_builder_BookBuilder_Map = Generalization(general=Map, specific=doc_builder_BookBuilder)

# Domain Model
domain_model = DomainModel(
    name="doc",
    types={doc_Test, doc_map_Map, MapContainer, NameRule, doc_map_NameRule, ExtensionMappingEntry, doc_map_Import, MapElement, doc_map_File, Import, doc_map_MapSection, map_MapContainer, map_MapElement, doc_map_MapElement, doc_map_Feature, doc_map_ResourceFactory, doc_map_ExtensionMappingEntry, ResourceFactory, doc_map_ContentGenerator, fragment_Content, doc_map_PatternRule, doc_map_IncludePatternRule, PatternRule, doc_map_ExcludePatternRule, Content, doc_map_MapContainer, doc_fragment_Fragment, Container, doc_fragment_Section, doc_fragment_Container, doc_fragment_Copyright, Author, doc_book_Book, BookContainer, Section, doc_fragment_PlainTextContent, doc_fragment_Content, doc_fragment_Author, doc_book_BookContainer, BookSection, Copyright, doc_book_BookSection, doc_builder_BookBuilder, Map, builder_PropertyEntry, doc_builder_PropertyEntry, NumberingStyle, RuleResult},
    associations={fileNameRules1, extensionMappings0, factory2, anyContent4, elements3, author7, section5, content12, sections14, authors8, copyright10, authors16, copyright18, properties21},
    generalizations={gen_doc_map_Map_MapContainer, gen_doc_map_Feature_Import, gen_doc_map_Import_MapElement, gen_doc_map_File_Import, gen_doc_map_MapSection_map_MapContainer, gen_doc_map_MapSection_map_MapElement, gen_doc_map_ContentGenerator_map_MapElement, gen_doc_map_ContentGenerator_fragment_Content, gen_doc_map_PatternRule_NameRule, gen_doc_map_IncludePatternRule_PatternRule, gen_doc_map_ExcludePatternRule_PatternRule, gen_doc_fragment_Fragment_Container, gen_doc_fragment_Section_Container, gen_doc_book_Book_BookContainer, gen_doc_fragment_PlainTextContent_Content, gen_doc_book_BookSection_BookContainer, gen_doc_builder_BookBuilder_Map},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)