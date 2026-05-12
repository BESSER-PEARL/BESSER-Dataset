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
latex_Styles = Class(name="latex_Styles")
latex_Abstracte = Class(name="latex_Abstracte")
latex_Document = Class(name="latex_Document")
latex_Body = Class(name="latex_Body")
latex_Bibliography = Class(name="latex_Bibliography")
latex_Packages = Class(name="latex_Packages")
latex_Commands = Class(name="latex_Commands")
latex_Title = Class(name="latex_Title")
latex_General = Class(name="latex_General")
latex_Begin = Class(name="latex_Begin")
latex_End = Class(name="latex_End")
latex_Section = Class(name="latex_Section")
latex_Figures = Class(name="latex_Figures")
latex_Enumerate = Class(name="latex_Enumerate")
latex_bibitem = Class(name="latex_bibitem")
latex_Beginbib = Class(name="latex_Beginbib")
latex_Endbib = Class(name="latex_Endbib")
latex_Subsection = Class(name="latex_Subsection")

# latex_Styles class attributes and methods
latex_Styles_styleprefix: Property = Property(name="styleprefix", type=StringType)
latex_Styles_stylesnames: Property = Property(name="stylesnames", type=StringType)
latex_Styles_stylenames: Property = Property(name="stylenames", type=StringType)
latex_Styles.attributes={latex_Styles_stylesnames, latex_Styles_stylenames, latex_Styles_styleprefix}

# latex_Abstracte class attributes and methods
latex_Abstracte_abstracttext: Property = Property(name="abstracttext", type=StringType)
latex_Abstracte_abstractprefix: Property = Property(name="abstractprefix", type=StringType)
latex_Abstracte.attributes={latex_Abstracte_abstracttext, latex_Abstracte_abstractprefix}

# latex_Document class attributes and methods
latex_Document_documenttype: Property = Property(name="documenttype", type=StringType)
latex_Document_prefix: Property = Property(name="prefix", type=StringType)
latex_Document_fontsize: Property = Property(name="fontsize", type=StringType)
latex_Document_papertype: Property = Property(name="papertype", type=StringType)
latex_Document.attributes={latex_Document_documenttype, latex_Document_prefix, latex_Document_papertype, latex_Document_fontsize}

# latex_Body class attributes and methods

# latex_Bibliography class attributes and methods
latex_Bibliography_bibstyle: Property = Property(name="bibstyle", type=StringType)
latex_Bibliography.attributes={latex_Bibliography_bibstyle}

# latex_Packages class attributes and methods
latex_Packages_packageprefix: Property = Property(name="packageprefix", type=StringType)
latex_Packages_packagetype: Property = Property(name="packagetype", type=StringType)
latex_Packages.attributes={latex_Packages_packagetype, latex_Packages_packageprefix}

# latex_Commands class attributes and methods
latex_Commands_number: Property = Property(name="number", type=FloatType)
latex_Commands_comprefix: Property = Property(name="comprefix", type=StringType)
latex_Commands_comname: Property = Property(name="comname", type=StringType)
latex_Commands_comtext: Property = Property(name="comtext", type=StringType)
latex_Commands.attributes={latex_Commands_comname, latex_Commands_comtext, latex_Commands_comprefix, latex_Commands_number}

# latex_Title class attributes and methods
latex_Title_titleprefix: Property = Property(name="titleprefix", type=StringType)
latex_Title_titletext: Property = Property(name="titletext", type=StringType)
latex_Title_authortext: Property = Property(name="authortext", type=StringType)
latex_Title.attributes={latex_Title_titleprefix, latex_Title_authortext, latex_Title_titletext}

# latex_General class attributes and methods
latex_General_genprefix: Property = Property(name="genprefix", type=StringType)
latex_General_genname: Property = Property(name="genname", type=StringType)
latex_General_gentext: Property = Property(name="gentext", type=StringType)
latex_General.attributes={latex_General_gentext, latex_General_genprefix, latex_General_genname}

# latex_Begin class attributes and methods
latex_Begin_beginprefix: Property = Property(name="beginprefix", type=StringType)
latex_Begin.attributes={latex_Begin_beginprefix}

# latex_End class attributes and methods
latex_End_endprefix: Property = Property(name="endprefix", type=StringType)
latex_End.attributes={latex_End_endprefix}

# latex_Section class attributes and methods
latex_Section_sectionprefix: Property = Property(name="sectionprefix", type=StringType)
latex_Section_sectionname: Property = Property(name="sectionname", type=StringType)
latex_Section_sectiontext: Property = Property(name="sectiontext", type=StringType)
latex_Section.attributes={latex_Section_sectionprefix, latex_Section_sectiontext, latex_Section_sectionname}

# latex_Figures class attributes and methods
latex_Figures_figprefix: Property = Property(name="figprefix", type=StringType)
latex_Figures_figcaption: Property = Property(name="figcaption", type=StringType)
latex_Figures_figname: Property = Property(name="figname", type=StringType)
latex_Figures.attributes={latex_Figures_figname, latex_Figures_figcaption, latex_Figures_figprefix}

# latex_Enumerate class attributes and methods
latex_Enumerate_enumprefix: Property = Property(name="enumprefix", type=StringType)
latex_Enumerate_enumtext: Property = Property(name="enumtext", type=StringType)
latex_Enumerate.attributes={latex_Enumerate_enumprefix, latex_Enumerate_enumtext}

# latex_bibitem class attributes and methods
latex_bibitem_bibprefix: Property = Property(name="bibprefix", type=StringType)
latex_bibitem_bibtext: Property = Property(name="bibtext", type=StringType)
latex_bibitem.attributes={latex_bibitem_bibprefix, latex_bibitem_bibtext}

# latex_Beginbib class attributes and methods
latex_Beginbib_Beginbibprefix: Property = Property(name="Beginbibprefix", type=StringType)
latex_Beginbib.attributes={latex_Beginbib_Beginbibprefix}

# latex_Endbib class attributes and methods
latex_Endbib_Endbibprefix: Property = Property(name="Endbibprefix", type=StringType)
latex_Endbib.attributes={latex_Endbib_Endbibprefix}

# latex_Subsection class attributes and methods
latex_Subsection_subsectionprefix: Property = Property(name="subsectionprefix", type=StringType)
latex_Subsection_subsectionname: Property = Property(name="subsectionname", type=StringType)
latex_Subsection_subsectiontext: Property = Property(name="subsectiontext", type=StringType)
latex_Subsection.attributes={latex_Subsection_subsectionprefix, latex_Subsection_subsectiontext, latex_Subsection_subsectionname}

# Relationships
containsstyles5: BinaryAssociation = BinaryAssociation(
    name="containsstyles5",
    ends={
        Property(name="latex_Styles", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document6", type=latex_Styles, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsabstract7: BinaryAssociation = BinaryAssociation(
    name="containsabstract7",
    ends={
        Property(name="latex_Abstracte", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document8", type=latex_Abstracte, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containsbody9: BinaryAssociation = BinaryAssociation(
    name="containsbody9",
    ends={
        Property(name="latex_Body", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document10", type=latex_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containspackages0: BinaryAssociation = BinaryAssociation(
    name="containspackages0",
    ends={
        Property(name="latex_Packages", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document", type=latex_Packages, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containscommands1: BinaryAssociation = BinaryAssociation(
    name="containscommands1",
    ends={
        Property(name="latex_Commands", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document2", type=latex_Commands, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containstitle3: BinaryAssociation = BinaryAssociation(
    name="containstitle3",
    ends={
        Property(name="latex_Title", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document4", type=latex_Title, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
titlecontainsgen17: BinaryAssociation = BinaryAssociation(
    name="titlecontainsgen17",
    ends={
        Property(name="latex_General", type=latex_Title, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Title18", type=latex_General, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsbib11: BinaryAssociation = BinaryAssociation(
    name="containsbib11",
    ends={
        Property(name="latex_Bibliography", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document12", type=latex_Bibliography, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
begindoc13: BinaryAssociation = BinaryAssociation(
    name="begindoc13",
    ends={
        Property(name="latex_Begin", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document14", type=latex_Begin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enddoc15: BinaryAssociation = BinaryAssociation(
    name="enddoc15",
    ends={
        Property(name="latex_End", type=latex_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Document16", type=latex_End, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Abscontainsgen19: BinaryAssociation = BinaryAssociation(
    name="Abscontainsgen19",
    ends={
        Property(name="latex_General21", type=latex_Abstracte, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Abstracte20", type=latex_General, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containssections22: BinaryAssociation = BinaryAssociation(
    name="containssections22",
    ends={
        Property(name="latex_Section", type=latex_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Body23", type=latex_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsfigures24: BinaryAssociation = BinaryAssociation(
    name="containsfigures24",
    ends={
        Property(name="latex_Figures", type=latex_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Body25", type=latex_Figures, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsenumerate26: BinaryAssociation = BinaryAssociation(
    name="containsenumerate26",
    ends={
        Property(name="latex_Enumerate", type=latex_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Body27", type=latex_Enumerate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bibcontainsgen28: BinaryAssociation = BinaryAssociation(
    name="bibcontainsgen28",
    ends={
        Property(name="latex_General30", type=latex_Bibliography, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Bibliography29", type=latex_General, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsbibitems31: BinaryAssociation = BinaryAssociation(
    name="containsbibitems31",
    ends={
        Property(name="latex_bibitem", type=latex_Bibliography, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Bibliography32", type=latex_bibitem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containbeginbib33: BinaryAssociation = BinaryAssociation(
    name="containbeginbib33",
    ends={
        Property(name="latex_Beginbib", type=latex_Bibliography, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Bibliography34", type=latex_Beginbib, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containendbib35: BinaryAssociation = BinaryAssociation(
    name="containendbib35",
    ends={
        Property(name="latex_Endbib", type=latex_Bibliography, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Bibliography36", type=latex_Endbib, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seccontainsgen37: BinaryAssociation = BinaryAssociation(
    name="seccontainsgen37",
    ends={
        Property(name="latex_General39", type=latex_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Section38", type=latex_General, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsubsections40: BinaryAssociation = BinaryAssociation(
    name="containsubsections40",
    ends={
        Property(name="latex_Subsection", type=latex_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Section41", type=latex_Subsection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containssubsections43: BinaryAssociation = BinaryAssociation(
    name="containssubsections43",
    ends={
        Property(name="latex_Subsection44", type=latex_Subsection, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Subsection42", type=latex_Subsection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subseccontainsgen45: BinaryAssociation = BinaryAssociation(
    name="subseccontainsgen45",
    ends={
        Property(name="latex_General47", type=latex_Subsection, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Subsection46", type=latex_General, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figcontainsgen48: BinaryAssociation = BinaryAssociation(
    name="figcontainsgen48",
    ends={
        Property(name="latex_General50", type=latex_Figures, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Figures49", type=latex_General, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumcontainsgen51: BinaryAssociation = BinaryAssociation(
    name="enumcontainsgen51",
    ends={
        Property(name="latex_General53", type=latex_Enumerate, multiplicity=Multiplicity(1, 1)),
        Property(name="latex_Enumerate52", type=latex_General, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="latex",
    types={latex_Styles, latex_Abstracte, latex_Document, latex_Body, latex_Bibliography, latex_Packages, latex_Commands, latex_Title, latex_General, latex_Begin, latex_End, latex_Section, latex_Figures, latex_Enumerate, latex_bibitem, latex_Beginbib, latex_Endbib, latex_Subsection},
    associations={containsstyles5, containsabstract7, containsbody9, containspackages0, containscommands1, containstitle3, titlecontainsgen17, containsbib11, begindoc13, enddoc15, Abscontainsgen19, containssections22, containsfigures24, containsenumerate26, bibcontainsgen28, containsbibitems31, containbeginbib33, containendbib35, seccontainsgen37, containsubsections40, containssubsections43, subseccontainsgen45, figcontainsgen48, enumcontainsgen51},
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