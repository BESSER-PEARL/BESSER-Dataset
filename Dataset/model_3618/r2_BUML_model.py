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
AddressPartType: Enumeration = Enumeration(
    name="AddressPartType",
    literals={
            EnumerationLiteral(name="AL"),
			EnumerationLiteral(name="ADL"),
			EnumerationLiteral(name="UNID"),
			EnumerationLiteral(name="UNIT"),
			EnumerationLiteral(name="DAL"),
			EnumerationLiteral(name="DMODID"),
			EnumerationLiteral(name="SAL"),
			EnumerationLiteral(name="BNR"),
			EnumerationLiteral(name="BNN"),
			EnumerationLiteral(name="BNS"),
			EnumerationLiteral(name="STR"),
			EnumerationLiteral(name="STB"),
			EnumerationLiteral(name="STTYP"),
			EnumerationLiteral(name="DIR"),
			EnumerationLiteral(name="DINST"),
			EnumerationLiteral(name="DINSTA"),
			EnumerationLiteral(name="DINSTQ"),
			EnumerationLiteral(name="DMOD"),
			EnumerationLiteral(name="CPA"),
			EnumerationLiteral(name="CTY"),
			EnumerationLiteral(name="DEL"),
			EnumerationLiteral(name="POB"),
			EnumerationLiteral(name="PRE"),
			EnumerationLiteral(name="STA"),
			EnumerationLiteral(name="ZIP"),
			EnumerationLiteral(name="DPID"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="CAR"),
			EnumerationLiteral(name="CEN"),
			EnumerationLiteral(name="CNT")
    }
)

CalendarCycle: Enumeration = Enumeration(
    name="CalendarCycle",
    literals={
            EnumerationLiteral(name="CY"),
			EnumerationLiteral(name="MY"),
			EnumerationLiteral(name="DM"),
			EnumerationLiteral(name="CD"),
			EnumerationLiteral(name="DY"),
			EnumerationLiteral(name="DW"),
			EnumerationLiteral(name="HD"),
			EnumerationLiteral(name="CH"),
			EnumerationLiteral(name="NH"),
			EnumerationLiteral(name="CN"),
			EnumerationLiteral(name="SN"),
			EnumerationLiteral(name="CM"),
			EnumerationLiteral(name="CW"),
			EnumerationLiteral(name="WM"),
			EnumerationLiteral(name="WY"),
			EnumerationLiteral(name="CS")
    }
)

Compression: Enumeration = Enumeration(
    name="Compression",
    literals={
            EnumerationLiteral(name="DF"),
			EnumerationLiteral(name="GZ"),
			EnumerationLiteral(name="ZL"),
			EnumerationLiteral(name="Z"),
			EnumerationLiteral(name="BZ"),
			EnumerationLiteral(name="Z7")
    }
)

EntityNamePartQualifier: Enumeration = Enumeration(
    name="EntityNamePartQualifier",
    literals={
            EnumerationLiteral(name="LS"),
			EnumerationLiteral(name="AC"),
			EnumerationLiteral(name="NB"),
			EnumerationLiteral(name="PR"),
			EnumerationLiteral(name="SFX"),
			EnumerationLiteral(name="HON"),
			EnumerationLiteral(name="BR"),
			EnumerationLiteral(name="AD"),
			EnumerationLiteral(name="SP"),
			EnumerationLiteral(name="MID"),
			EnumerationLiteral(name="CL"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="PFX")
    }
)

EntityNamePartType: Enumeration = Enumeration(
    name="EntityNamePartType",
    literals={
            EnumerationLiteral(name="FAM"),
			EnumerationLiteral(name="GIV"),
			EnumerationLiteral(name="TITLE"),
			EnumerationLiteral(name="DEL")
    }
)

EntityNameUse: Enumeration = Enumeration(
    name="EntityNameUse",
    literals={
            EnumerationLiteral(name="C"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="T"),
			EnumerationLiteral(name="I"),
			EnumerationLiteral(name="P"),
			EnumerationLiteral(name="ABC"),
			EnumerationLiteral(name="IDE"),
			EnumerationLiteral(name="SYL"),
			EnumerationLiteral(name="ANON"),
			EnumerationLiteral(name="A"),
			EnumerationLiteral(name="R"),
			EnumerationLiteral(name="OLD"),
			EnumerationLiteral(name="DN"),
			EnumerationLiteral(name="M"),
			EnumerationLiteral(name="PHON"),
			EnumerationLiteral(name="SRCH")
    }
)

IntegrityCheckAlgorithm: Enumeration = Enumeration(
    name="IntegrityCheckAlgorithm",
    literals={
            EnumerationLiteral(name="SHA1"),
			EnumerationLiteral(name="SHA256")
    }
)

PostalAddressUse: Enumeration = Enumeration(
    name="PostalAddressUse",
    literals={
            EnumerationLiteral(name="H"),
			EnumerationLiteral(name="HP"),
			EnumerationLiteral(name="HV"),
			EnumerationLiteral(name="WP"),
			EnumerationLiteral(name="DIR"),
			EnumerationLiteral(name="PUB"),
			EnumerationLiteral(name="BAD"),
			EnumerationLiteral(name="PHYS"),
			EnumerationLiteral(name="PST"),
			EnumerationLiteral(name="TMP"),
			EnumerationLiteral(name="ABC"),
			EnumerationLiteral(name="IDE"),
			EnumerationLiteral(name="SYL"),
			EnumerationLiteral(name="SRCH"),
			EnumerationLiteral(name="SNDX"),
			EnumerationLiteral(name="PHON")
    }
)

TelecommunicationAddressUse: Enumeration = Enumeration(
    name="TelecommunicationAddressUse",
    literals={
            EnumerationLiteral(name="H"),
			EnumerationLiteral(name="HP"),
			EnumerationLiteral(name="HV"),
			EnumerationLiteral(name="WP"),
			EnumerationLiteral(name="DIR"),
			EnumerationLiteral(name="PUB"),
			EnumerationLiteral(name="BAD"),
			EnumerationLiteral(name="TMP"),
			EnumerationLiteral(name="AS"),
			EnumerationLiteral(name="EC"),
			EnumerationLiteral(name="MC"),
			EnumerationLiteral(name="PG")
    }
)

TelecommunicationCapability: Enumeration = Enumeration(
    name="TelecommunicationCapability",
    literals={
            EnumerationLiteral(name="voice"),
			EnumerationLiteral(name="fax"),
			EnumerationLiteral(name="data"),
			EnumerationLiteral(name="tty"),
			EnumerationLiteral(name="sms")
    }
)

# Classes
r2_AD = Class(name="r2::AD")
ANY = Class(name="ANY")
r2_ADXP = Class(name="r2::ADXP")
XP = Class(name="XP")
r2_ANY = Class(name="r2::ANY", is_abstract=True)
HXIT = Class(name="HXIT")
r2_BL = Class(name="r2::BL")
r2_ST = Class(name="r2::ST")
r2_CD = Class(name="r2::CD")
r2_CO = Class(name="r2::CO")
QTY = Class(name="QTY")
r2_ED = Class(name="r2::ED")
r2_EObject = Class(name="r2::EObject")
r2_CS = Class(name="r2::CS")
r2_TEL = Class(name="r2::TEL")
r2_EN = Class(name="r2::EN")
r2_ENXP = Class(name="r2::ENXP")
r2_INT = Class(name="r2::INT")
r2_HXIT = Class(name="r2::HXIT", is_abstract=True)
r2_II = Class(name="r2::II")
r2_IVLCO = Class(name="r2::IVLCO")
IVL = Class(name="IVL")
r2_IVL = Class(name="r2::IVL")
QSET = Class(name="QSET")
r2_IVLINT = Class(name="r2::IVLINT")
r2_PQ = Class(name="r2::PQ")
r2_IVLPQ = Class(name="r2::IVLPQ")
r2_IVLQTY = Class(name="r2::IVLQTY")
r2_QTY = Class(name="r2::QTY", is_abstract=True)
r2_REAL = Class(name="r2::REAL")
r2_IVLREAL = Class(name="r2::IVLREAL")
r2_PIVLTS = Class(name="r2::PIVLTS")
r2_IVLTS = Class(name="r2::IVLTS")
r2_TS = Class(name="r2::TS")
r2_RTO = Class(name="r2::RTO")
r2_QSET = Class(name="r2::QSET", is_abstract=True)
r2_XP = Class(name="r2::XP")

# r2_AD class attributes and methods
r2_AD_use: Property = Property(name="use", type=StringType)
r2_AD.attributes={r2_AD_use}

# ANY class attributes and methods

# r2_ADXP class attributes and methods
r2_ADXP_type: Property = Property(name="type", type=StringType)
r2_ADXP.attributes={r2_ADXP_type}

# XP class attributes and methods

# r2_ANY class attributes and methods

# HXIT class attributes and methods

# r2_BL class attributes and methods
r2_BL_value: Property = Property(name="value", type=StringType)
r2_BL.attributes={r2_BL_value}

# r2_ST class attributes and methods
r2_ST_value: Property = Property(name="value", type=StringType)
r2_ST.attributes={r2_ST_value}

# r2_CD class attributes and methods
r2_CD_codeSystemName: Property = Property(name="codeSystemName", type=StringType)
r2_CD_codeSystemVersion: Property = Property(name="codeSystemVersion", type=StringType)
r2_CD_valueSet: Property = Property(name="valueSet", type=StringType)
r2_CD_valueSetVersion: Property = Property(name="valueSetVersion", type=StringType)
r2_CD_code: Property = Property(name="code", type=StringType)
r2_CD_codeSystem: Property = Property(name="codeSystem", type=StringType)
r2_CD.attributes={r2_CD_valueSetVersion, r2_CD_valueSet, r2_CD_codeSystemVersion, r2_CD_codeSystemName, r2_CD_code, r2_CD_codeSystem}

# r2_CO class attributes and methods
r2_CO_value: Property = Property(name="value", type=StringType)
r2_CO.attributes={r2_CO_value}

# QTY class attributes and methods

# r2_ED class attributes and methods
r2_ED_integrityCheck: Property = Property(name="integrityCheck", type=StringType)
r2_ED_data: Property = Property(name="data", type=StringType)
r2_ED_language: Property = Property(name="language", type=StringType)
r2_ED_mediaType: Property = Property(name="mediaType", type=StringType)
r2_ED_value: Property = Property(name="value", type=StringType)
r2_ED_charset: Property = Property(name="charset", type=StringType)
r2_ED_compression: Property = Property(name="compression", type=StringType)
r2_ED_integrityCheckAlgorithm: Property = Property(name="integrityCheckAlgorithm", type=StringType)
r2_ED.attributes={r2_ED_data, r2_ED_charset, r2_ED_integrityCheck, r2_ED_integrityCheckAlgorithm, r2_ED_value, r2_ED_mediaType, r2_ED_compression, r2_ED_language}

# r2_EObject class attributes and methods

# r2_CS class attributes and methods
r2_CS_code: Property = Property(name="code", type=StringType)
r2_CS.attributes={r2_CS_code}

# r2_TEL class attributes and methods
r2_TEL_value: Property = Property(name="value", type=StringType)
r2_TEL_capabilities: Property = Property(name="capabilities", type=StringType)
r2_TEL_use: Property = Property(name="use", type=StringType)
r2_TEL.attributes={r2_TEL_capabilities, r2_TEL_value, r2_TEL_use}

# r2_EN class attributes and methods
r2_EN_use: Property = Property(name="use", type=StringType)
r2_EN.attributes={r2_EN_use}

# r2_ENXP class attributes and methods
r2_ENXP_qualifier: Property = Property(name="qualifier", type=StringType)
r2_ENXP_type: Property = Property(name="type", type=StringType)
r2_ENXP.attributes={r2_ENXP_type, r2_ENXP_qualifier}

# r2_INT class attributes and methods
r2_INT_value: Property = Property(name="value", type=StringType)
r2_INT.attributes={r2_INT_value}

# r2_HXIT class attributes and methods

# r2_II class attributes and methods
r2_II_identifierName: Property = Property(name="identifierName", type=StringType)
r2_II_root: Property = Property(name="root", type=StringType)
r2_II_extension: Property = Property(name="extension", type=StringType)
r2_II.attributes={r2_II_identifierName, r2_II_extension, r2_II_root}

# r2_IVLCO class attributes and methods
r2_IVLCO_highClosed: Property = Property(name="highClosed", type=StringType)
r2_IVLCO_lowClosed: Property = Property(name="lowClosed", type=StringType)
r2_IVLCO.attributes={r2_IVLCO_highClosed, r2_IVLCO_lowClosed}

# IVL class attributes and methods

# r2_IVL class attributes and methods

# QSET class attributes and methods

# r2_IVLINT class attributes and methods
r2_IVLINT_highClosed: Property = Property(name="highClosed", type=StringType)
r2_IVLINT_lowClosed: Property = Property(name="lowClosed", type=StringType)
r2_IVLINT.attributes={r2_IVLINT_lowClosed, r2_IVLINT_highClosed}

# r2_PQ class attributes and methods
r2_PQ_unit: Property = Property(name="unit", type=StringType)
r2_PQ_value: Property = Property(name="value", type=StringType)
r2_PQ.attributes={r2_PQ_value, r2_PQ_unit}

# r2_IVLPQ class attributes and methods
r2_IVLPQ_highClosed: Property = Property(name="highClosed", type=StringType)
r2_IVLPQ_lowClosed: Property = Property(name="lowClosed", type=StringType)
r2_IVLPQ.attributes={r2_IVLPQ_highClosed, r2_IVLPQ_lowClosed}

# r2_IVLQTY class attributes and methods
r2_IVLQTY_highClosed: Property = Property(name="highClosed", type=StringType)
r2_IVLQTY_lowClosed: Property = Property(name="lowClosed", type=StringType)
r2_IVLQTY.attributes={r2_IVLQTY_lowClosed, r2_IVLQTY_highClosed}

# r2_QTY class attributes and methods

# r2_REAL class attributes and methods
r2_REAL_value: Property = Property(name="value", type=StringType)
r2_REAL.attributes={r2_REAL_value}

# r2_IVLREAL class attributes and methods
r2_IVLREAL_highClosed: Property = Property(name="highClosed", type=StringType)
r2_IVLREAL_lowClosed: Property = Property(name="lowClosed", type=StringType)
r2_IVLREAL.attributes={r2_IVLREAL_lowClosed, r2_IVLREAL_highClosed}

# r2_PIVLTS class attributes and methods
r2_PIVLTS_alignment: Property = Property(name="alignment", type=StringType)
r2_PIVLTS_isFlexible: Property = Property(name="isFlexible", type=StringType)
r2_PIVLTS.attributes={r2_PIVLTS_isFlexible, r2_PIVLTS_alignment}

# r2_IVLTS class attributes and methods
r2_IVLTS_highClosed: Property = Property(name="highClosed", type=StringType)
r2_IVLTS_lowClosed: Property = Property(name="lowClosed", type=StringType)
r2_IVLTS.attributes={r2_IVLTS_lowClosed, r2_IVLTS_highClosed}

# r2_TS class attributes and methods
r2_TS_value: Property = Property(name="value", type=StringType)
r2_TS.attributes={r2_TS_value}

# r2_RTO class attributes and methods

# r2_QSET class attributes and methods

# r2_XP class attributes and methods
r2_XP_value: Property = Property(name="value", type=StringType)
r2_XP.attributes={r2_XP_value}

# Relationships
part0: BinaryAssociation = BinaryAssociation(
    name="part0",
    ends={
        Property(name="r2_ADXP", type=r2_AD, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_AD", type=r2_ADXP, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
displayName1: BinaryAssociation = BinaryAssociation(
    name="displayName1",
    ends={
        Property(name="r2_ST", type=r2_CD, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_CD", type=r2_ST, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalText2: BinaryAssociation = BinaryAssociation(
    name="originalText2",
    ends={
        Property(name="r2_ST4", type=r2_CD, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_CD3", type=r2_ST, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
translation6: BinaryAssociation = BinaryAssociation(
    name="translation6",
    ends={
        Property(name="r2_CD7", type=r2_CD, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_CD5", type=r2_CD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code8: BinaryAssociation = BinaryAssociation(
    name="code8",
    ends={
        Property(name="r2_CD9", type=r2_CO, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_CO", type=r2_CD, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference11: BinaryAssociation = BinaryAssociation(
    name="reference11",
    ends={
        Property(name="r2_ED12", type=r2_TEL, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="r2_TEL", type=r2_ED, multiplicity=Multiplicity(1, 1))
    }
)
xml10: BinaryAssociation = BinaryAssociation(
    name="xml10",
    ends={
        Property(name="r2_EObject", type=r2_ED, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_ED", type=r2_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description13: BinaryAssociation = BinaryAssociation(
    name="description13",
    ends={
        Property(name="r2_ST15", type=r2_ED, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_ED14", type=r2_ST, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part16: BinaryAssociation = BinaryAssociation(
    name="part16",
    ends={
        Property(name="r2_ENXP", type=r2_EN, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_EN", type=r2_ENXP, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
low22: BinaryAssociation = BinaryAssociation(
    name="low22",
    ends={
        Property(name="r2_INT", type=r2_IVLINT, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLINT", type=r2_INT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
low17: BinaryAssociation = BinaryAssociation(
    name="low17",
    ends={
        Property(name="r2_CO18", type=r2_IVLCO, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLCO", type=r2_CO, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
high19: BinaryAssociation = BinaryAssociation(
    name="high19",
    ends={
        Property(name="r2_CO21", type=r2_IVLCO, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLCO20", type=r2_CO, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
low26: BinaryAssociation = BinaryAssociation(
    name="low26",
    ends={
        Property(name="r2_PQ", type=r2_IVLPQ, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLPQ", type=r2_PQ, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
high27: BinaryAssociation = BinaryAssociation(
    name="high27",
    ends={
        Property(name="r2_PQ29", type=r2_IVLPQ, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLPQ28", type=r2_PQ, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
high23: BinaryAssociation = BinaryAssociation(
    name="high23",
    ends={
        Property(name="r2_INT25", type=r2_IVLINT, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLINT24", type=r2_INT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
low30: BinaryAssociation = BinaryAssociation(
    name="low30",
    ends={
        Property(name="r2_QTY", type=r2_IVLQTY, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLQTY", type=r2_QTY, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
high31: BinaryAssociation = BinaryAssociation(
    name="high31",
    ends={
        Property(name="r2_QTY33", type=r2_IVLQTY, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLQTY32", type=r2_QTY, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
low34: BinaryAssociation = BinaryAssociation(
    name="low34",
    ends={
        Property(name="r2_REAL", type=r2_IVLREAL, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLREAL", type=r2_REAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
high35: BinaryAssociation = BinaryAssociation(
    name="high35",
    ends={
        Property(name="r2_REAL37", type=r2_IVLREAL, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLREAL36", type=r2_REAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
low38: BinaryAssociation = BinaryAssociation(
    name="low38",
    ends={
        Property(name="r2_TS", type=r2_IVLTS, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLTS", type=r2_TS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
high39: BinaryAssociation = BinaryAssociation(
    name="high39",
    ends={
        Property(name="r2_TS41", type=r2_IVLTS, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_IVLTS40", type=r2_TS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phase42: BinaryAssociation = BinaryAssociation(
    name="phase42",
    ends={
        Property(name="r2_IVLTS43", type=r2_PIVLTS, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_PIVLTS", type=r2_IVLTS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
period44: BinaryAssociation = BinaryAssociation(
    name="period44",
    ends={
        Property(name="r2_PQ46", type=r2_PIVLTS, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_PIVLTS45", type=r2_PQ, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
frequency47: BinaryAssociation = BinaryAssociation(
    name="frequency47",
    ends={
        Property(name="r2_RTO", type=r2_PIVLTS, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_PIVLTS48", type=r2_RTO, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
count49: BinaryAssociation = BinaryAssociation(
    name="count49",
    ends={
        Property(name="r2_INT51", type=r2_PIVLTS, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_PIVLTS50", type=r2_INT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numerator52: BinaryAssociation = BinaryAssociation(
    name="numerator52",
    ends={
        Property(name="r2_QTY54", type=r2_RTO, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_RTO53", type=r2_QTY, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
denominator55: BinaryAssociation = BinaryAssociation(
    name="denominator55",
    ends={
        Property(name="r2_QTY57", type=r2_RTO, multiplicity=Multiplicity(1, 1)),
        Property(name="r2_RTO56", type=r2_QTY, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_r2_AD_ANY = Generalization(general=ANY, specific=r2_AD)
gen_r2_ANY_HXIT = Generalization(general=HXIT, specific=r2_ANY)
gen_r2_BL_ANY = Generalization(general=ANY, specific=r2_BL)
gen_r2_ADXP_XP = Generalization(general=XP, specific=r2_ADXP)
gen_r2_CD_ANY = Generalization(general=ANY, specific=r2_CD)
gen_r2_CO_QTY = Generalization(general=QTY, specific=r2_CO)
gen_r2_ED_ANY = Generalization(general=ANY, specific=r2_ED)
gen_r2_CS_ANY = Generalization(general=ANY, specific=r2_CS)
gen_r2_EN_ANY = Generalization(general=ANY, specific=r2_EN)
gen_r2_ENXP_XP = Generalization(general=XP, specific=r2_ENXP)
gen_r2_II_ANY = Generalization(general=ANY, specific=r2_II)
gen_r2_IVLCO_IVL = Generalization(general=IVL, specific=r2_IVLCO)
gen_r2_INT_QTY = Generalization(general=QTY, specific=r2_INT)
gen_r2_IVL_QSET = Generalization(general=QSET, specific=r2_IVL)
gen_r2_IVLINT_IVL = Generalization(general=IVL, specific=r2_IVLINT)
gen_r2_IVLPQ_IVL = Generalization(general=IVL, specific=r2_IVLPQ)
gen_r2_IVLQTY_IVL = Generalization(general=IVL, specific=r2_IVLQTY)
gen_r2_IVLREAL_IVL = Generalization(general=IVL, specific=r2_IVLREAL)
gen_r2_PIVLTS_QTY = Generalization(general=QTY, specific=r2_PIVLTS)
gen_r2_IVLTS_IVL = Generalization(general=IVL, specific=r2_IVLTS)
gen_r2_QSET_ANY = Generalization(general=ANY, specific=r2_QSET)
gen_r2_QTY_ANY = Generalization(general=ANY, specific=r2_QTY)
gen_r2_PQ_QTY = Generalization(general=QTY, specific=r2_PQ)
gen_r2_REAL_QTY = Generalization(general=QTY, specific=r2_REAL)
gen_r2_RTO_QTY = Generalization(general=QTY, specific=r2_RTO)
gen_r2_ST_ANY = Generalization(general=ANY, specific=r2_ST)
gen_r2_TEL_ANY = Generalization(general=ANY, specific=r2_TEL)
gen_r2_TS_QTY = Generalization(general=QTY, specific=r2_TS)

# Domain Model
domain_model = DomainModel(
    name="r2",
    types={r2_AD, ANY, r2_ADXP, XP, r2_ANY, HXIT, r2_BL, r2_ST, r2_CD, r2_CO, QTY, r2_ED, r2_EObject, r2_CS, r2_TEL, r2_EN, r2_ENXP, r2_INT, r2_HXIT, r2_II, r2_IVLCO, IVL, r2_IVL, QSET, r2_IVLINT, r2_PQ, r2_IVLPQ, r2_IVLQTY, r2_QTY, r2_REAL, r2_IVLREAL, r2_PIVLTS, r2_IVLTS, r2_TS, r2_RTO, r2_QSET, r2_XP, AddressPartType, CalendarCycle, Compression, EntityNamePartQualifier, EntityNamePartType, EntityNameUse, IntegrityCheckAlgorithm, PostalAddressUse, TelecommunicationAddressUse, TelecommunicationCapability},
    associations={part0, displayName1, originalText2, translation6, code8, reference11, xml10, description13, part16, low22, low17, high19, low26, high27, high23, low30, high31, low34, high35, low38, high39, phase42, period44, frequency47, count49, numerator52, denominator55},
    generalizations={gen_r2_AD_ANY, gen_r2_ANY_HXIT, gen_r2_BL_ANY, gen_r2_ADXP_XP, gen_r2_CD_ANY, gen_r2_CO_QTY, gen_r2_ED_ANY, gen_r2_CS_ANY, gen_r2_EN_ANY, gen_r2_ENXP_XP, gen_r2_II_ANY, gen_r2_IVLCO_IVL, gen_r2_INT_QTY, gen_r2_IVL_QSET, gen_r2_IVLINT_IVL, gen_r2_IVLPQ_IVL, gen_r2_IVLQTY_IVL, gen_r2_IVLREAL_IVL, gen_r2_PIVLTS_QTY, gen_r2_IVLTS_IVL, gen_r2_QSET_ANY, gen_r2_QTY_ANY, gen_r2_PQ_QTY, gen_r2_REAL_QTY, gen_r2_RTO_QTY, gen_r2_ST_ANY, gen_r2_TEL_ANY, gen_r2_TS_QTY},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)