from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Quotes(Enum):
    quote = "quote"
    quotes = "quotes"
class Orders(Enum):
    asc = "asc"
    dsc = "dsc"
class Nulls(Enum):
    null = "null"
    nulls = "nulls"
class UPSISwitches(Enum):
    upsi0 = "upsi0"
    upsi1 = "upsi1"
    upsi2 = "upsi2"
    upsi3 = "upsi3"
    upsi4 = "upsi4"
    upsi5 = "upsi5"
    upsi6 = "upsi6"
    upsi7 = "upsi7"
class Spaces(Enum):
    space = "space"
    spaces = "spaces"
class SystemOutputs(Enum):
    sysout = "sysout"
    syslist = "syslist"
    syslst = "syslst"
class UseStatementTokens(Enum):
    global = "global"
    after = "after"
    standard = "standard"
    error = "error"
    exception = "exception"
    procedure = "procedure"
    on = "on"
    input = "input"
    output = "output"
    extend = "extend"
    for = "for"
    debugging = "debugging"
    all = "all"
    procedures = "procedures"
    beginning = "beginning"
    ending = "ending"
    file = "file"
    reel = "reel"
    unit = "unit"
    label = "label"
    io = "io"
class Channels(Enum):
    c1 = "c1"
    c2 = "c2"
    c3 = "c3"
    c4 = "c4"
    c5 = "c5"
    c6 = "c6"
    c7 = "c7"
    c8 = "c8"
    c9 = "c9"
    c10 = "c10"
    c11 = "c11"
    c12 = "c12"
class EOP(Enum):
    eop = "eop"
    endOfPage = "endOfPage"
class DataDescriptionInfo(Enum):
    just = "just"
    right = "right"
    sign = "sign"
    is = "is"
    leading = "leading"
    trailing = "trailing"
    separate = "separate"
    character = "character"
    date = "date"
    format = "format"
    synchronized = "synchronized"
    sync = "sync"
    left = "left"
    blank = "blank"
    when = "when"
    zero = "zero"
    zeros = "zeros"
    zeroes = "zeroes"
    justified = "justified"
class IOControlDescriptionInfo(Enum):
    rerun = "rerun"
    on = "on"
    of = "of"
    record = "record"
    records = "records"
    every = "every"
    same = "same"
    area = "area"
    for = "for"
    multiple = "multiple"
    file = "file"
    tape = "tape"
    contains = "contains"
    position = "position"
    apply = "apply"
    writeOnly = "writeOnly"
    sort = "sort"
    sortMerge = "sortMerge"
    reel = "reel"
    unit = "unit"
class OpenStatementTokens(Enum):
    reversed = "reversed"
    with = "with"
    no = "no"
    rewind = "rewind"
class ExitLabels(Enum):
    program = "program"
    paragraph = "paragraph"
    method = "method"
class Zeroes(Enum):
    zero = "zero"
    zeros = "zeros"
    zeroes = "zeroes"
class RepositoryDescriptionInfo(Enum):
    class = "class"
    is = "is"
class IOTypes(Enum):
    input = "input"
    output = "output"
    io = "io"
    extend = "extend"
class Occurrences(Enum):
    all = "all"
    leading = "leading"
    first = "first"
class InvokeStatementTokens(Enum):
    self = "self"
    super = "super"
    new = "new"
    using = "using"
    by = "by"
    value = "value"
    length = "length"
    of = "of"
    returning = "returning"
class SelectStatementClauses(Enum):
    with = "with"
    dynamic = "dynamic"
    organization = "organization"
    duplicates = "duplicates"
    indexed = "indexed"
    alternate = "alternate"
    record = "record"
    key = "key"
    relative = "relative"
    delimiter = "delimiter"
    standard1 = "standard1"
    padding = "padding"
    character = "character"
    reserve = "reserve"
    area = "area"
    areas = "areas"
    access = "access"
    mode = "mode"
    is = "is"
    sequential = "sequential"
    random = "random"
class SQLStatementTokens(Enum):
    include = "include"
    select = "select"
    declare = "declare"
    from = "from"
    insert = "insert"
    into = "into"
    update = "update"
    delete = "delete"
class SpecialNamesClauses(Enum):
    decimalPoint = "decimalPoint"
    is = "is"
    comma = "comma"
    xmlSchema = "xmlSchema"
class SystemPunchDevices(Enum):
    syspunch = "syspunch"
    syspch = "syspch"
class ObjectComputerDescriptionInfo(Enum):
    memory = "memory"
    size = "size"
    words = "words"
    characters = "characters"
    modules = "modules"
    segment = "segment"
    program = "program"
    collating = "collating"
    sequence = "sequence"
    segmentLimit = "segmentLimit"
class HighValues(Enum):
    highValue = "highValue"
    highValues = "highValues"
class Positions(Enum):
    before = "before"
    after = "after"
class SortPhraseTokens(Enum):
    with = "with"
    in = "in"
    order = "order"
    sequence = "sequence"
    duplicates = "duplicates"
    collating = "collating"
    is = "is"
class ProgramDescriptionInfo(Enum):
    author = "author"
    installation = "installation"
    dateWritten = "dateWritten"
    dateCompleted = "dateCompleted"
    security = "security"
class FileDescriptionInfo(Enum):
    block = "block"
    contains = "contains"
    lines = "lines"
    with = "with"
    footing = "footing"
    at = "at"
    top = "top"
    bottom = "bottom"
    varying = "varying"
    in = "in"
    size = "size"
    from = "from"
    depending = "depending"
    on = "on"
    mode = "mode"
    recording = "recording"
    f = "f"
    v = "v"
    to = "to"
    u = "u"
    characters = "characters"
    s = "s"
    value = "value"
    records = "records"
    of = "of"
    codeSet = "codeSet"
    identification = "identification"
    is = "is"
    id = "id"
    data = "data"
    report = "report"
    reports = "reports"
    record = "record"
    are = "are"
    label = "label"
    omitted = "omitted"
    standard = "standard"
    linage = "linage"
class EncodingTypes(Enum):
    alphabetic = "alphabetic"
    alphanumeric = "alphanumeric"
    alphanumericEdited = "alphanumericEdited"
    national = "national"
    nationalEdited = "nationalEdited"
    numeric = "numeric"
    numericEdited = "numericEdited"
    dbcs = "dbcs"
    egcs = "egcs"
class Usages(Enum):
    binary = "binary"
    computational = "computational"
    comp = "comp"
    display = "display"
    display1 = "display1"
    index = "index"
    packedDecimal = "packedDecimal"
    computational1 = "computational1"
    comp1 = "comp1"
    computational2 = "computational2"
    comp2 = "comp2"
    computational3 = "computational3"
    comp3 = "comp3"
    computational4 = "computational4"
    comp4 = "comp4"
    computational5 = "computational5"
    comp5 = "comp5"
    pointer = "pointer"
    procedurePointer = "procedurePointer"
    functionPointer = "functionPointer"
    national = "national"
class ThroughPhrase(Enum):
    through = "through"
    thru = "thru"
class Selects(Enum):
    s1 = "s1"
    s2 = "s2"
    s3 = "s3"
    s4 = "s4"
    s5 = "s5"
class CloseStatementTokens(Enum):
    with = "with"
    no = "no"
    rewind = "rewind"
    lock = "lock"
    reel = "reel"
    unit = "unit"
    for = "for"
    removal = "removal"
class Corresponding(Enum):
    corr = "corr"
    corresponding = "corresponding"
class CICSStatementTokens(Enum):
    ts = "ts"
    queue = "queue"
    qname = "qname"
    openpar = "openpar"
    closepar = "closepar"
    sysid = "sysid"
    sys = "sys"
    set = "set"
    into = "into"
    length = "length"
    item = "item"
    next = "next"
    numitems = "numitems"
    td = "td"
    writeq = "writeq"
    from = "from"
    rewrite = "rewrite"
    nosuspend = "nosuspend"
    main = "main"
    auxiliary = "auxiliary"
    deleteq = "deleteq"
    read = "read"
    file = "file"
    dataset = "dataset"
    ridfld = "ridfld"
    keylength = "keylength"
    generic = "generic"
    gteq = "gteq"
    equal = "equal"
    uncommitted = "uncommitted"
    consistent = "consistent"
    repeatable = "repeatable"
    update = "update"
    token = "token"
    rba = "rba"
    xrba = "xrba"
    rrn = "rrn"
    write = "write"
    xctl = "xctl"
    load = "load"
    start = "start"
    tr = "tr"
    massinsert = "massinsert"
    program = "program"
    commarea = "commarea"
    datalength = "datalength"
    synconreturn = "synconreturn"
    transid = "transid"
    inputmsg = "inputmsg"
    inputmsglen = "inputmsglen"
    channel = "channel"
class Properties(Enum):
    initial = "initial"
    common = "common"
    recursive = "recursive"
class SortingOrder(Enum):
    dsc = "dsc"
    asc = "asc"
class PredefinedAlphabetTypes(Enum):
    native = "native"
    standard1 = "standard1"
    standard2 = "standard2"
    ebcdic = "ebcdic"
class Adjustings(Enum):
    up = "up"
    down = "down"
class FileDescriptors(Enum):
    fd = "fd"
    sd = "sd"
class LowValues(Enum):
    lowValue = "lowValue"
    lowValues = "lowValues"
class SystemInputs(Enum):
    sysin = "sysin"
    sysipt = "sysipt"
class Status(Enum):
    on = "on"
    off = "off"
class PictureStringCharacters(Enum):
    numeric = "numeric"
    assumedDecimalPoint = "assumedDecimalPoint"
    alphabetic = "alphabetic"
    national = "national"
    credit = "credit"
    debit = "debit"
    zero = "zero"
    plus = "plus"
    negative = "negative"
    exponent = "exponent"
    period = "period"
    comma = "comma"
    dollar = "dollar"
    asterik = "asterik"
    slash = "slash"
    escape = "escape"
    any = "any"
    blank = "blank"
    sign = "sign"
    leadingZero = "leadingZero"
    decimalPoint = "decimalPoint"
class AcceptStatementTokens(Enum):
    from = "from"
    date = "date"
    day = "day"
    dow = "dow"
    time = "time"
    dateformat1 = "dateformat1"
    dateformat2 = "dateformat2"


############################################
# Definition of Classes
############################################

class cobol_strings_Location:

    def __init__(self, position: str, initial: bool, cobol_strings_Location: "PrimaryOperand" = None):
        self.position = position
        self.initial = initial
        self.cobol_strings_Location = cobol_strings_Location
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def cobol_strings_Location(self):
        return self.__cobol_strings_Location

    @cobol_strings_Location.setter
    def cobol_strings_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_strings_Location__cobol_strings_Location", None)
        self.__cobol_strings_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimaryOperand405"):
                opp_val = getattr(old_value, "PrimaryOperand405", None)
                if opp_val == self:
                    setattr(old_value, "PrimaryOperand405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimaryOperand405"):
                opp_val = getattr(value, "PrimaryOperand405", None)
                setattr(value, "PrimaryOperand405", self)

class strings_Replacement:

    pass
class strings_Occurrence:

    pass
class cobol_strings_ReplacementOccurrence(strings_Occurrence, strings_Replacement):

    pass
class strings_Tallying:

    pass
class cobol_strings_TallyingOccurrence(strings_Occurrence, strings_Tallying):

    pass
class cobol_strings_Occurrence(ABC):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class ManipulatedStrings:

    pass
class cobol_strings_SplittedString(ManipulatedStrings):

    pass
class cobol_strings_ConcatenatingStrings(ManipulatedStrings):

    pass
class cobol_strings_String(ABC):

    pass
class Location:

    pass
class String:

    pass
class cobol_strings_ManipulatedStrings(String):

    pass
class cobol_strings_StringManipulation(String):

    pass
class StringManipulation:

    pass
class cobol_strings_Replacement(StringManipulation):

    pass
class cobol_strings_Tallying(StringManipulation):

    pass
class NotErrorHandler:

    pass
class cobol_handlers_NotOnException(NotErrorHandler):

    pass
class cobol_handlers_NotAtEndOfPage(NotErrorHandler):

    pass
class cobol_handlers_NotOnOverflow(NotErrorHandler):

    pass
class cobol_handlers_NotInvalidKey(NotErrorHandler):

    pass
class cobol_handlers_NotAtEnd(NotErrorHandler):

    pass
class cobol_handlers_NotOnSizeError(NotErrorHandler):

    pass
class cobol_functions_Argumentable(ABC):

    pass
class Argument:

    pass
class cobol_functions_ByValueArgument(Argument):

    pass
class cobol_functions_OmittedArgument(Argument):

    pass
class cobol_functions_ByContentArgument(Argument):

    pass
class cobol_functions_ByReferenceArgument(Argument):

    pass
class cobol_functions_Argument(ABC):

    pass
class cobol_labels_Label(ABC):

    pass
class cobol_labels_Procedure(ABC):

    pass
class Procedure:

    pass
class ProcedureRangeChild:

    pass
class cobol_labels_ProcedureLabel(ProcedureRangeChild):

    pass
class cobol_verbs_Verb(ABC):

    pass
class Verb:

    pass
class cobol_verbs_Is(Verb):

    pass
class DeclarativeSection:

    pass
class cobol_declaratives_Declaratives:

    pass
class Parameter:

    pass
class cobol_parameters_ByReferenceParameter(Parameter):

    pass
class cobol_parameters_ByValueParameter(Parameter):

    pass
class cobol_parameters_Parametrizable(ABC):

    pass
class cobol_files_FileStatus:

    pass
class FileStatus:

    pass
class cobol_tables_TableDimension:

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class AdditionalIndexName:

    pass
class cobol_tables_KeyName:

    def __init__(self, keyOrder: str, cobol_tables_KeyName: set["IdentifierReference"] = None):
        self.keyOrder = keyOrder
        self.cobol_tables_KeyName = cobol_tables_KeyName if cobol_tables_KeyName is not None else set()
        
    @property
    def keyOrder(self) -> str:
        return self.__keyOrder

    @keyOrder.setter
    def keyOrder(self, keyOrder: str):
        self.__keyOrder = keyOrder

    @property
    def cobol_tables_KeyName(self):
        return self.__cobol_tables_KeyName

    @cobol_tables_KeyName.setter
    def cobol_tables_KeyName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_tables_KeyName__cobol_tables_KeyName", None)
        self.__cobol_tables_KeyName = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IdentifierReference357"):
                    opp_val = getattr(item, "IdentifierReference357", None)
                    
                    if opp_val == self:
                        setattr(item, "IdentifierReference357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IdentifierReference357"):
                    opp_val = getattr(item, "IdentifierReference357", None)
                    
                    setattr(item, "IdentifierReference357", self)
                    

class KeyName:

    pass
class IndexName:

    pass
class TableDimension:

    pass
class dataitems_DataItem:

    pass
class cobol_specialnames_SpecialNameStatement(ABC):

    pass
class AlphabetNameReference:

    pass
class SymbolicCharacter:

    pass
class SpecialName:

    pass
class cobol_specialnames_SymbolicCharacter(SpecialName):

    pass
class cobol_specialnames_MnemonicName(SpecialName):

    pass
class cobol_specialnames_AlphabetType(ABC):

    pass
class specialnames_MnemonicName:

    pass
class AlphabetType:

    pass
class cobol_specialnames_PredefinedAlphabetType(AlphabetType):

    def __init__(self, value: str, AlphabetType: "cobol_specialnames_AlphabetName"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_specialnames_CodeNameAlphabetType(AlphabetType):

    def __init__(self, value: str, AlphabetType: "cobol_specialnames_AlphabetName"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_specialnames_ExplicitAlphabetType(AlphabetType):

    pass
class specialnames_SpecialNameStatement:

    pass
class cobol_specialnames_UPSISwitchIs(specialnames_MnemonicName, specialnames_SpecialNameStatement):

    pass
class cobol_specialnames_SystemDeviceIs(specialnames_MnemonicName, specialnames_SpecialNameStatement):

    pass
class ConditionName:

    pass
class cobol_specialnames_OffStatus(ConditionName):

    pass
class cobol_specialnames_OnStatus(ConditionName):

    pass
class specialnames_SpecialName:

    pass
class cobol_specialnames_CurrencySign(specialnames_SpecialName, specialnames_SpecialNameStatement):

    def __init__(self, pictureSymbol: str, cobol_specialnames_CurrencySign: "Literal" = None):
        self.pictureSymbol = pictureSymbol
        self.cobol_specialnames_CurrencySign = cobol_specialnames_CurrencySign
        
    @property
    def pictureSymbol(self) -> str:
        return self.__pictureSymbol

    @pictureSymbol.setter
    def pictureSymbol(self, pictureSymbol: str):
        self.__pictureSymbol = pictureSymbol

    @property
    def cobol_specialnames_CurrencySign(self):
        return self.__cobol_specialnames_CurrencySign

    @cobol_specialnames_CurrencySign.setter
    def cobol_specialnames_CurrencySign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_specialnames_CurrencySign__cobol_specialnames_CurrencySign", None)
        self.__cobol_specialnames_CurrencySign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Literal"):
                opp_val = getattr(old_value, "Literal", None)
                if opp_val == self:
                    setattr(old_value, "Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Literal"):
                opp_val = getattr(value, "Literal", None)
                setattr(value, "Literal", self)

class cobol_specialnames_AlphabetName(specialnames_SpecialName, specialnames_SpecialNameStatement):

    pass
class cobol_specialnames_ClassName(specialnames_SpecialName, specialnames_SpecialNameStatement):

    pass
class DataName:

    pass
class cobol_dataitems_RenamingDataName(DataName):

    pass
class DataItemAttribute:

    pass
class cobol_dataitems_Redefines(DataItemAttribute):

    pass
class cobol_dataitems_PictureString(DataItemAttribute):

    def __init__(self, picture: str, DataItemAttribute363: "cobol_files_FileName", DataItemAttribute: "cobol_dataitems_DataItem"):
        self.picture = picture
        
    @property
    def picture(self) -> str:
        return self.__picture

    @picture.setter
    def picture(self, picture: str):
        self.__picture = picture

class references_ReferenceableElement:

    pass
class cobol_dataitems_GroupUsage(DataItemAttribute):

    pass
class cobol_dataitems_Usage(DataItemAttribute):

    def __init__(self, usage: str, isNative: bool, DataItemAttribute363: "cobol_files_FileName", DataItemAttribute: "cobol_dataitems_DataItem"):
        self.usage = usage
        self.isNative = isNative
        
    @property
    def isNative(self) -> bool:
        return self.__isNative

    @isNative.setter
    def isNative(self, isNative: bool):
        self.__isNative = isNative

    @property
    def usage(self) -> str:
        return self.__usage

    @usage.setter
    def usage(self, usage: str):
        self.__usage = usage

class cobol_dataitems_DataItemAttribute(ABC):

    pass
class cobol_dataitems_Value(DataItemAttribute):

    pass
class cobol_dataitems_External(DataItemAttribute):

    pass
class cobol_dataitems_Global(DataItemAttribute):

    pass
class RangeExpression:

    pass
class SystemDevice:

    pass
class cobol_environments_Console(SystemDevice):

    pass
class cobol_environments_SystemLogicalOutput(SystemDevice):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_environments_SystemPunchDevice(SystemDevice):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_environments_AdvancedFunctionPrinting(SystemDevice):

    pass
class cobol_environments_Pocket(SystemDevice):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_environments_SuppressSpacing(SystemDevice):

    pass
class cobol_environments_Channel(SystemDevice):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_environments_SystemLogicalInput(SystemDevice):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Register:

    pass
class cobol_registers_LengthOf(Register):

    pass
class cobol_registers_ShiftOut(Register):

    pass
class cobol_registers_AddressOf(Register):

    pass
class cobol_registers_WhenCompiled(Register):

    pass
class cobol_registers_ReturnCode(Register):

    pass
class cobol_registers_ShiftIn(Register):

    pass
class SortPhraseWater:

    pass
class cobol_water_SortPhraseToken(SortPhraseWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class OpenStatementWater:

    pass
class cobol_water_OpenStatementToken(OpenStatementWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class CloseStatementWater:

    pass
class cobol_water_CloseStatementToken(CloseStatementWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class InvokeStatementWater:

    pass
class cobol_water_InvokeStatementToken(InvokeStatementWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class UseStatementWater:

    pass
class cobol_water_UseStatementToken(UseStatementWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class AcceptStatementWater:

    pass
class cobol_environments_Environment(AcceptStatementWater):

    pass
class cobol_water_AcceptStatementToken(AcceptStatementWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class CICSStatementWater:

    pass
class cobol_water_CICSStatementToken(CICSStatementWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class SQLStatementWater:

    pass
class cobol_water_SQLStatementToken(SQLStatementWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class RepositoryParagraphWater:

    pass
class cobol_water_RepositoryDescription(RepositoryParagraphWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class IOControlParagraphWater:

    pass
class cobol_water_IOControlDescription(IOControlParagraphWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class DataDescriptorWater:

    pass
class cobol_water_DataDescription(DataDescriptorWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class FileDescriptorWater:

    pass
class cobol_water_FileDescription(FileDescriptorWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class SelectStatementWater:

    pass
class cobol_water_SelectStatementClause(SelectStatementWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ObjectComputerParagraphWater:

    pass
class cobol_water_PriorityNumber(ObjectComputerParagraphWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_water_ObjectComputerDescription(ObjectComputerParagraphWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class IdentificationDivisionWater:

    pass
class cobol_water_ProgramDescription(IdentificationDivisionWater):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_water_Water(ABC):

    pass
class Water:

    pass
class cobol_water_IdentificationDivisionWater(Water):

    pass
class cobol_water_DataDescriptorWater(Water):

    pass
class cobol_water_ObjectComputerParagraphWater(Water):

    pass
class cobol_water_CloseStatementWater(Water):

    pass
class cobol_water_SpecialNamesParagraphWater(Water):

    pass
class cobol_water_UseStatementWater(Water):

    pass
class cobol_water_CICSStatementWater(Water):

    pass
class cobol_water_AcceptStatementWater(Water):

    pass
class cobol_water_SortPhraseWater(Water):

    pass
class cobol_water_RepositoryParagraphWater(Water):

    pass
class cobol_water_IOControlParagraphWater(Water):

    pass
class cobol_water_FileDescriptorWater(Water):

    pass
class cobol_water_SelectStatementWater(Water):

    pass
class cobol_water_OpenStatementWater(Water):

    pass
class cobol_water_SQLStatementWater(Water):

    pass
class cobol_water_InvokeStatementWater(Water):

    pass
class cobol_water_IncompleteElement(ABC):

    pass
class Label:

    pass
class cobol_labels_StopLabel(Label):

    pass
class cobol_labels_ProcedureRangeLabel(Label):

    pass
class cobol_ios_IODirectives(ABC):

    pass
class ios_OutputDirective:

    pass
class cobol_identifiers_ReferenceModifier:

    pass
class DirectSubscript:

    pass
class cobol_identifiers_All(DirectSubscript):

    pass
class Qualifier:

    pass
class Subscript:

    pass
class identifiers_Identifier:

    pass
class ReferenceModifier:

    pass
class water_SortPhraseWater:

    pass
class water_DataDescriptorWater:

    pass
class water_UseStatementWater:

    pass
class ios_FileDirective:

    pass
class cobol_ios_OutputFile(ios_OutputDirective, ios_FileDirective):

    pass
class IODirectives:

    pass
class cobol_ios_FileDirective(IODirectives):

    pass
class cobol_ios_ProcedureDirective(IODirectives):

    pass
class cobol_ios_OutputDirective(IODirectives):

    pass
class cobol_ios_InputDirective(IODirectives):

    pass
class ios_ProcedureDirective:

    pass
class cobol_ios_OutputProcedure(ios_ProcedureDirective, ios_OutputDirective):

    pass
class ios_InputDirective:

    pass
class cobol_ios_InputFile(ios_InputDirective, ios_FileDirective):

    pass
class cobol_ios_InputProcedure(ios_ProcedureDirective, ios_InputDirective):

    pass
class cobol_identifiers_DirectSubscript(Subscript):

    pass
class cobol_identifiers_RelativeSubscript(Subscript):

    pass
class VaryingUntilCondition:

    pass
class cobol_statements_AfterUntilCondition(VaryingUntilCondition):

    pass
class Conditional:

    pass
class cobol_statements_VaryingUntilCondition(Conditional):

    pass
class IOFile:

    pass
class cobol_statements_IOFileDescriptor:

    def __init__(self, type: str, cobol_statements_IOFileDescriptor: set["IOFile"] = None):
        self.type = type
        self.cobol_statements_IOFileDescriptor = cobol_statements_IOFileDescriptor if cobol_statements_IOFileDescriptor is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cobol_statements_IOFileDescriptor(self):
        return self.__cobol_statements_IOFileDescriptor

    @cobol_statements_IOFileDescriptor.setter
    def cobol_statements_IOFileDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_IOFileDescriptor__cobol_statements_IOFileDescriptor", None)
        self.__cobol_statements_IOFileDescriptor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IOFile"):
                    opp_val = getattr(item, "IOFile", None)
                    
                    if opp_val == self:
                        setattr(item, "IOFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IOFile"):
                    opp_val = getattr(item, "IOFile", None)
                    
                    setattr(item, "IOFile", self)
                    

class water_SQLStatementWater:

    pass
class water_IdentificationDivisionWater:

    pass
class cobol_water_Dot(water_SQLStatementWater, water_IdentificationDivisionWater):

    pass
class water_RepositoryParagraphWater:

    pass
class water_AcceptStatementWater:

    pass
class cobol_identifiers_Subscript(ABC):

    pass
class Tallying:

    pass
class cobol_strings_AnyCharacter(Tallying):

    pass
class cobol_strings_SpecificCharacter(Tallying):

    pass
class cobol_statements_TallyingIn:

    pass
class IncompleteElement:

    pass
class cobol_files_SelectStatement(IncompleteElement):

    def __init__(self, isOptional: bool, externalFileNames: str, cobol_files_SelectStatement: "FileStatus" = None, cobol_files_SelectStatement369: "FileNameReference" = None):
        self.isOptional = isOptional
        self.externalFileNames = externalFileNames
        self.cobol_files_SelectStatement = cobol_files_SelectStatement
        self.cobol_files_SelectStatement369 = cobol_files_SelectStatement369
        
    @property
    def externalFileNames(self) -> str:
        return self.__externalFileNames

    @externalFileNames.setter
    def externalFileNames(self, externalFileNames: str):
        self.__externalFileNames = externalFileNames

    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

    @property
    def cobol_files_SelectStatement369(self):
        return self.__cobol_files_SelectStatement369

    @cobol_files_SelectStatement369.setter
    def cobol_files_SelectStatement369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_files_SelectStatement__cobol_files_SelectStatement369", None)
        self.__cobol_files_SelectStatement369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FileNameReference370"):
                opp_val = getattr(old_value, "FileNameReference370", None)
                if opp_val == self:
                    setattr(old_value, "FileNameReference370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FileNameReference370"):
                opp_val = getattr(value, "FileNameReference370", None)
                setattr(value, "FileNameReference370", self)

    @property
    def cobol_files_SelectStatement(self):
        return self.__cobol_files_SelectStatement

    @cobol_files_SelectStatement.setter
    def cobol_files_SelectStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_files_SelectStatement__cobol_files_SelectStatement", None)
        self.__cobol_files_SelectStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FileStatus"):
                opp_val = getattr(old_value, "FileStatus", None)
                if opp_val == self:
                    setattr(old_value, "FileStatus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FileStatus"):
                opp_val = getattr(value, "FileStatus", None)
                setattr(value, "FileStatus", self)

class cobol_statements_IOFile(IncompleteElement):

    pass
class statements_PerformUntilCondition:

    pass
class IOFileDescriptor:

    pass
class cobol_statements_KeyDescriptor:

    def __init__(self, order: str, cobol_statements_KeyDescriptor: set["IdentifierReference"] = None):
        self.order = order
        self.cobol_statements_KeyDescriptor = cobol_statements_KeyDescriptor if cobol_statements_KeyDescriptor is not None else set()
        
    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def cobol_statements_KeyDescriptor(self):
        return self.__cobol_statements_KeyDescriptor

    @cobol_statements_KeyDescriptor.setter
    def cobol_statements_KeyDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_KeyDescriptor__cobol_statements_KeyDescriptor", None)
        self.__cobol_statements_KeyDescriptor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IdentifierReference267"):
                    opp_val = getattr(item, "IdentifierReference267", None)
                    
                    if opp_val == self:
                        setattr(item, "IdentifierReference267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IdentifierReference267"):
                    opp_val = getattr(item, "IdentifierReference267", None)
                    
                    setattr(item, "IdentifierReference267", self)
                    

class statements_FileIOStatement:

    pass
class KeyDescriptor:

    pass
class OutputDirective:

    pass
class InputDirective:

    pass
class statements_PerformNestedStatement:

    pass
class cobol_statements_PerformNestedStatementUntilCondition(statements_PerformUntilCondition, statements_PerformNestedStatement):

    pass
class AfterUntilCondition:

    pass
class statements_VaryingUntilCondition:

    pass
class statements_PerformFixedTimes:

    pass
class cobol_statements_PerformNestedStatementFixedTimes(statements_PerformFixedTimes, statements_PerformNestedStatement):

    pass
class statements_PerformProcedure:

    pass
class cobol_statements_PerformProcedureUntilCondition(statements_PerformUntilCondition, statements_PerformProcedure):

    pass
class cobol_statements_PerformProcedureFixedTimes(statements_PerformFixedTimes, statements_PerformProcedure):

    pass
class cobol_statements_SwitchStatus:

    def __init__(self, status: str, cobol_statements_SwitchStatus: set["MnemonicNameReference"] = None):
        self.status = status
        self.cobol_statements_SwitchStatus = cobol_statements_SwitchStatus if cobol_statements_SwitchStatus is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def cobol_statements_SwitchStatus(self):
        return self.__cobol_statements_SwitchStatus

    @cobol_statements_SwitchStatus.setter
    def cobol_statements_SwitchStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_SwitchStatus__cobol_statements_SwitchStatus", None)
        self.__cobol_statements_SwitchStatus = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MnemonicNameReference247"):
                    opp_val = getattr(item, "MnemonicNameReference247", None)
                    
                    if opp_val == self:
                        setattr(item, "MnemonicNameReference247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MnemonicNameReference247"):
                    opp_val = getattr(item, "MnemonicNameReference247", None)
                    
                    setattr(item, "MnemonicNameReference247", self)
                    

class Write:

    pass
class cobol_statements_Rewrite(Write):

    pass
class MnemonicNameReference:

    pass
class IntegerLiteral:

    pass
class SplittedString:

    pass
class TallyingIn:

    pass
class NestedStatement:

    pass
class cobol_handlers_Handler(NestedStatement):

    pass
class cobol_statements_EvaluateCase(NestedStatement):

    pass
class ExpressionList:

    pass
class EvaluateCase:

    pass
class cobol_statements_OtherEvaluateCase(EvaluateCase):

    pass
class cobol_statements_NormalEvaluateCase(EvaluateCase):

    pass
class functions_Argumentable:

    pass
class SearchStatement:

    pass
class cobol_statements_BinarySearch(SearchStatement):

    pass
class cobol_statements_SerialSearch(SearchStatement):

    pass
class NormalEvaluateCase:

    pass
class Replacement:

    pass
class cobol_strings_AnyCharacterBySpecificCharacter(Replacement):

    pass
class cobol_strings_SpecificCharacterBySpecificCharacter(Replacement):

    pass
class statements_IOStatement:

    pass
class ConcatenatingStrings:

    pass
class IndexNameReference:

    pass
class SwitchStatus:

    pass
class SetStatement:

    pass
class cobol_statements_SetIndexName(SetStatement):

    def __init__(self, adjust: str, cobol_statements_SetIndexName: set["IndexNameReference"] = None):
        self.adjust = adjust
        self.cobol_statements_SetIndexName = cobol_statements_SetIndexName if cobol_statements_SetIndexName is not None else set()
        
    @property
    def adjust(self) -> str:
        return self.__adjust

    @adjust.setter
    def adjust(self, adjust: str):
        self.__adjust = adjust

    @property
    def cobol_statements_SetIndexName(self):
        return self.__cobol_statements_SetIndexName

    @cobol_statements_SetIndexName.setter
    def cobol_statements_SetIndexName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_SetIndexName__cobol_statements_SetIndexName", None)
        self.__cobol_statements_SetIndexName = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IndexNameReference"):
                    opp_val = getattr(item, "IndexNameReference", None)
                    
                    if opp_val == self:
                        setattr(item, "IndexNameReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IndexNameReference"):
                    opp_val = getattr(item, "IndexNameReference", None)
                    
                    setattr(item, "IndexNameReference", self)
                    

class cobol_statements_Set(SetStatement):

    pass
class cobol_statements_SetSwitches(SetStatement):

    pass
class FileNameReference:

    pass
class Handler:

    pass
class cobol_handlers_OnOverflow(Handler):

    pass
class cobol_handlers_AtEnd(Handler):

    pass
class cobol_handlers_OnException(Handler):

    pass
class cobol_handlers_AtEndOfPage(Handler):

    def __init__(self, eop: str, Handler395: "cobol_handlers_NotErrorHandler", Handler: "cobol_statements_ErrorHandled"):
        self.eop = eop
        
    @property
    def eop(self) -> str:
        return self.__eop

    @eop.setter
    def eop(self, eop: str):
        self.__eop = eop

class cobol_handlers_NotErrorHandler(Handler):

    pass
class cobol_handlers_InvalidKey(Handler):

    pass
class cobol_handlers_OnSizeError(Handler):

    pass
class cobol_statements_ErrorHandled(ABC):

    pass
class AssignmentExpression:

    pass
class Environment:

    pass
class cobol_environments_SystemDevice(Environment):

    pass
class cobol_environments_UPSI(Environment):

    def __init__(self, value: str, Environment: "cobol_statements_Display", Environment339: "cobol_specialnames_MnemonicName"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class StopLabel:

    pass
class cobol_labels_Run(StopLabel):

    pass
class cobol_statements_Conditional(ABC):

    pass
class statements_Conditional:

    pass
class PrimaryOperand:

    pass
class cobol_registers_Register(PrimaryOperand):

    pass
class cobol_statements_NestedStatement(ABC):

    pass
class Jump:

    pass
class cobol_statements_Continue(Jump):

    pass
class cobol_statements_GoBack(Jump):

    pass
class cobol_statements_GoTo(Jump):

    pass
class cobol_statements_NextSentence(Jump):

    pass
class ProcedureRangeLabel:

    pass
class cobol_labels_ProcedureRangeChild(ProcedureRangeLabel):

    pass
class cobol_labels_ProcedureRange(ProcedureRangeLabel):

    pass
class Perform:

    pass
class cobol_statements_PerformFixedTimes(Perform):

    pass
class cobol_statements_PerformProcedure(Perform):

    pass
class statements_NestedStatement:

    pass
class statements_Perform:

    pass
class cobol_statements_PerformUntilCondition(statements_Perform, statements_VaryingUntilCondition):

    def __init__(self, position: str, cobol_statements_PerformUntilCondition: set["Condition"] = None):
        self.position = position
        self.cobol_statements_PerformUntilCondition = cobol_statements_PerformUntilCondition if cobol_statements_PerformUntilCondition is not None else set()
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def cobol_statements_PerformUntilCondition(self):
        return self.__cobol_statements_PerformUntilCondition

    @cobol_statements_PerformUntilCondition.setter
    def cobol_statements_PerformUntilCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_PerformUntilCondition__cobol_statements_PerformUntilCondition", None)
        self.__cobol_statements_PerformUntilCondition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Condition249"):
                    opp_val = getattr(item, "Condition249", None)
                    
                    if opp_val == self:
                        setattr(item, "Condition249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Condition249"):
                    opp_val = getattr(item, "Condition249", None)
                    
                    setattr(item, "Condition249", self)
                    

class cobol_statements_PerformNestedStatement(statements_Perform, statements_NestedStatement):

    pass
class Identifier:

    pass
class ArithmeticOperand:

    pass
class cobol_operands_RoundedIdentifier(ArithmeticOperand):

    pass
class ArithmeticStatement:

    pass
class cobol_statements_Divide(ArithmeticStatement):

    pass
class cobol_statements_Subtract(ArithmeticStatement):

    pass
class cobol_statements_Multiply(ArithmeticStatement):

    pass
class cobol_statements_Add(ArithmeticStatement):

    pass
class statements_ErrorHandled:

    pass
class statements_Statement:

    pass
class cobol_statements_Delete(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_Start(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_Write(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_Call(functions_Argumentable, statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_Condition(statements_Statement, statements_NestedStatement, statements_Conditional):

    pass
class cobol_statements_String(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_Return(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_Read(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_Unstring(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_SearchStatement(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_Compute(statements_Statement, statements_ErrorHandled):

    pass
class cobol_statements_ArithmeticStatement(statements_Statement, statements_ErrorHandled):

    def __init__(self, corresponding: str, cobol_statements_ArithmeticStatement: set["ArithmeticOperand"] = None, cobol_statements_ArithmeticStatement128: set["ArithmeticOperand"] = None):
        self.corresponding = corresponding
        self.cobol_statements_ArithmeticStatement = cobol_statements_ArithmeticStatement if cobol_statements_ArithmeticStatement is not None else set()
        self.cobol_statements_ArithmeticStatement128 = cobol_statements_ArithmeticStatement128 if cobol_statements_ArithmeticStatement128 is not None else set()
        
    @property
    def corresponding(self) -> str:
        return self.__corresponding

    @corresponding.setter
    def corresponding(self, corresponding: str):
        self.__corresponding = corresponding

    @property
    def cobol_statements_ArithmeticStatement(self):
        return self.__cobol_statements_ArithmeticStatement

    @cobol_statements_ArithmeticStatement.setter
    def cobol_statements_ArithmeticStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_ArithmeticStatement__cobol_statements_ArithmeticStatement", None)
        self.__cobol_statements_ArithmeticStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArithmeticOperand"):
                    opp_val = getattr(item, "ArithmeticOperand", None)
                    
                    if opp_val == self:
                        setattr(item, "ArithmeticOperand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArithmeticOperand"):
                    opp_val = getattr(item, "ArithmeticOperand", None)
                    
                    setattr(item, "ArithmeticOperand", self)
                    

    @property
    def cobol_statements_ArithmeticStatement128(self):
        return self.__cobol_statements_ArithmeticStatement128

    @cobol_statements_ArithmeticStatement128.setter
    def cobol_statements_ArithmeticStatement128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_ArithmeticStatement__cobol_statements_ArithmeticStatement128", None)
        self.__cobol_statements_ArithmeticStatement128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArithmeticOperand129"):
                    opp_val = getattr(item, "ArithmeticOperand129", None)
                    
                    if opp_val == self:
                        setattr(item, "ArithmeticOperand129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArithmeticOperand129"):
                    opp_val = getattr(item, "ArithmeticOperand129", None)
                    
                    setattr(item, "ArithmeticOperand129", self)
                    

class cobol_statements_Statement(ABC):

    def __init__(self, endVerb: bool, cobol_statements_Statement: "Statement" = None):
        self.endVerb = endVerb
        self.cobol_statements_Statement = cobol_statements_Statement
        
    @property
    def endVerb(self) -> bool:
        return self.__endVerb

    @endVerb.setter
    def endVerb(self, endVerb: bool):
        self.__endVerb = endVerb

    @property
    def cobol_statements_Statement(self):
        return self.__cobol_statements_Statement

    @cobol_statements_Statement.setter
    def cobol_statements_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_Statement__cobol_statements_Statement", None)
        self.__cobol_statements_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement125"):
                opp_val = getattr(old_value, "Statement125", None)
                if opp_val == self:
                    setattr(old_value, "Statement125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement125"):
                opp_val = getattr(value, "Statement125", None)
                setattr(value, "Statement125", self)

class cobol_operands_Operand(ABC):

    pass
class ReplacementOperand:

    pass
class cobol_operands_Encoding(ReplacementOperand):

    def __init__(self, type: str, ReplacementOperand: "cobol_strings_Replacement", ReplacementOperand414: "cobol_strings_SpecificCharacterBySpecificCharacter"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Operand:

    pass
class cobol_operands_ArithmeticOperand(Operand):

    pass
class cobol_operands_ReplacementOperand(Operand):

    pass
class operands_ArithmeticOperand:

    pass
class arithmetics_PrimaryExpression:

    pass
class operands_Operand:

    pass
class operands_ReplacementOperand:

    pass
class cobol_operands_PrimaryOperand(operands_Operand, arithmetics_PrimaryExpression, operands_ReplacementOperand, operands_ArithmeticOperand):

    pass
class sentences_StatementContainer:

    pass
class Sentence:

    pass
class cobol_sentences_ExitProcedure(Sentence):

    pass
class cobol_sentences_AlteredGoTo(Sentence):

    pass
class cobol_sentences_EntrySentence(Sentence):

    pass
class cobol_sentences_EmptySentence(Sentence):

    pass
class cobol_sentences_StatementContainer(ABC):

    pass
class FileName:

    pass
class DataItem:

    pass
class cobol_dataitems_ConditionName(DataItem):

    pass
class cobol_dataitems_RecordName(DataItem):

    pass
class cobol_dataitems_DataName(DataItem):

    pass
class Statement:

    pass
class cobol_statements_Initialize(Statement):

    pass
class cobol_statements_Perform(Statement):

    pass
class cobol_statements_Exit(Statement):

    def __init__(self, exitLabel: str, Statement121: "cobol_sentences_StatementContainer", Statement152: "cobol_statements_Condition", Statement: "cobol_sections_DataDivisionSection", Statement146: "cobol_statements_NestedStatement", Statement125: "cobol_statements_Statement"):
        self.exitLabel = exitLabel
        
    @property
    def exitLabel(self) -> str:
        return self.__exitLabel

    @exitLabel.setter
    def exitLabel(self, exitLabel: str):
        self.__exitLabel = exitLabel

class cobol_statements_Execute(Statement):

    def __init__(self, water: str, Statement121: "cobol_sentences_StatementContainer", Statement152: "cobol_statements_Condition", Statement: "cobol_sections_DataDivisionSection", Statement146: "cobol_statements_NestedStatement", Statement125: "cobol_statements_Statement"):
        self.water = water
        
    @property
    def water(self) -> str:
        return self.__water

    @water.setter
    def water(self, water: str):
        self.__water = water

class cobol_statements_Replace(Statement):

    def __init__(self, replaceSwitch: bool, Statement121: "cobol_sentences_StatementContainer", Statement152: "cobol_statements_Condition", Statement: "cobol_sections_DataDivisionSection", Statement146: "cobol_statements_NestedStatement", Statement125: "cobol_statements_Statement"):
        self.replaceSwitch = replaceSwitch
        
    @property
    def replaceSwitch(self) -> bool:
        return self.__replaceSwitch

    @replaceSwitch.setter
    def replaceSwitch(self, replaceSwitch: bool):
        self.__replaceSwitch = replaceSwitch

class cobol_statements_Evaluate(Statement):

    pass
class cobol_statements_Cancel(Statement):

    pass
class cobol_statements_Jump(Statement):

    pass
class cobol_statements_Stop(Statement):

    pass
class cobol_statements_Display(Statement):

    pass
class cobol_statements_FileIOStatement(Statement):

    pass
class cobol_statements_Inspect(Statement):

    pass
class cobol_statements_SetStatement(Statement):

    pass
class cobol_statements_Move(Statement):

    def __init__(self, corresponding: str, cobol_statements_Move: set["PrimaryOperand"] = None, cobol_statements_Move149: set["PrimaryOperand"] = None, Statement121: "cobol_sentences_StatementContainer", Statement152: "cobol_statements_Condition", Statement: "cobol_sections_DataDivisionSection", Statement146: "cobol_statements_NestedStatement", Statement125: "cobol_statements_Statement"):
        self.corresponding = corresponding
        self.cobol_statements_Move = cobol_statements_Move if cobol_statements_Move is not None else set()
        self.cobol_statements_Move149 = cobol_statements_Move149 if cobol_statements_Move149 is not None else set()
        
    @property
    def corresponding(self) -> str:
        return self.__corresponding

    @corresponding.setter
    def corresponding(self, corresponding: str):
        self.__corresponding = corresponding

    @property
    def cobol_statements_Move149(self):
        return self.__cobol_statements_Move149

    @cobol_statements_Move149.setter
    def cobol_statements_Move149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_Move__cobol_statements_Move149", None)
        self.__cobol_statements_Move149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PrimaryOperand150"):
                    opp_val = getattr(item, "PrimaryOperand150", None)
                    
                    if opp_val == self:
                        setattr(item, "PrimaryOperand150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PrimaryOperand150"):
                    opp_val = getattr(item, "PrimaryOperand150", None)
                    
                    setattr(item, "PrimaryOperand150", self)
                    

    @property
    def cobol_statements_Move(self):
        return self.__cobol_statements_Move

    @cobol_statements_Move.setter
    def cobol_statements_Move(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_statements_Move__cobol_statements_Move", None)
        self.__cobol_statements_Move = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PrimaryOperand"):
                    opp_val = getattr(item, "PrimaryOperand", None)
                    
                    if opp_val == self:
                        setattr(item, "PrimaryOperand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PrimaryOperand"):
                    opp_val = getattr(item, "PrimaryOperand", None)
                    
                    setattr(item, "PrimaryOperand", self)
                    

class cobol_statements_Release(Statement):

    pass
class cobol_statements_IOStatement(Statement):

    pass
class EnvironmentDivisionSection:

    pass
class cobol_sections_ConfigurationSection(EnvironmentDivisionSection):

    pass
class cobol_sections_IOSection(EnvironmentDivisionSection):

    pass
class SpecialNamesParagraphWater:

    pass
class cobol_water_SpecialNamesClause(SpecialNamesParagraphWater):

    def __init__(self, value: str, SpecialNamesParagraphWater: "cobol_paragraphs_SpecialNamesParagraph"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class DataDivisionSection:

    pass
class cobol_sections_FileSection(DataDivisionSection):

    pass
class cobol_sections_LocalStorageSection(DataDivisionSection):

    pass
class cobol_sections_LinkageStorageSection(DataDivisionSection):

    pass
class cobol_sections_WorkingStorageSection(DataDivisionSection):

    pass
class identifiers_IdentifierReference:

    pass
class cobol_references_Qualifiable(ABC):

    pass
class cobol_references_ConditionName(ABC):

    pass
class ElementReference:

    pass
class cobol_identifiers_Qualifier(ElementReference):

    pass
class cobol_references_AlphabetNameReference(ElementReference):

    pass
class IdentifierReference:

    pass
class cobol_references_IndexNameReference(IdentifierReference):

    pass
class references_IdentifierReferenceQualifier:

    pass
class cobol_references_DataNameReference(references_IdentifierReferenceQualifier, identifiers_IdentifierReference):

    pass
class references_ConditionName:

    pass
class cobol_references_ConditionNameReference(references_ConditionName, identifiers_IdentifierReference):

    pass
class references_Qualifiable:

    pass
class cobol_identifiers_LinageCounter(references_Qualifiable, identifiers_Identifier):

    pass
class references_ElementReference:

    pass
class cobol_references_IdentifierReferenceQualifier(references_Qualifiable, references_ElementReference):

    pass
class cobol_specialnames_SymbolicCharacterStatement(references_ElementReference, specialnames_SpecialNameStatement):

    pass
class cobol_identifiers_IdentifierReference(references_Qualifiable, references_ElementReference, identifiers_Identifier):

    pass
class cobol_references_FileNameReference(references_IdentifierReferenceQualifier, references_ElementReference):

    pass
class cobol_references_MnemonicNameReference(references_Qualifiable, references_ElementReference):

    pass
class cobol_references_SpecialNamesConditionNameReference(references_ElementReference, references_Qualifiable, references_ConditionName):

    pass
class Reference:

    pass
class cobol_references_ElementReference(Reference):

    pass
class ReferenceableElement:

    pass
class cobol_specialnames_SpecialName(ReferenceableElement):

    pass
class cobol_tables_AdditionalIndexName(ReferenceableElement):

    pass
class cobol_parameters_Parameter(ReferenceableElement):

    pass
class cobol_references_Reference(ABC):

    pass
class cobol_paragraphs_DebuggingMode:

    pass
class SpecialNameStatement:

    pass
class paragraphs_IOSectionParagraph:

    pass
class SelectStatement:

    pass
class IOSectionParagraph:

    pass
class cobol_paragraphs_FileControlParagraph(IOSectionParagraph):

    pass
class paragraphs_ConfigurationSectionParagraph:

    pass
class DebuggingMode:

    pass
class ConfigurationSectionParagraph:

    pass
class cobol_paragraphs_SpecialNamesParagraph(ConfigurationSectionParagraph):

    pass
class cobol_paragraphs_SourceComputerParagraph(ConfigurationSectionParagraph):

    pass
class labels_Procedure:

    pass
class GreaterThanOrEqual:

    pass
class cobol_operators_GTEQSign(GreaterThanOrEqual):

    pass
class cobol_operators_GTEQPhrase(GreaterThanOrEqual):

    pass
class GreaterThan:

    pass
class cobol_operators_GTSign(GreaterThan):

    pass
class cobol_operators_GTPhrase(GreaterThan):

    pass
class LessThanOrEqual:

    pass
class cobol_operators_LTEQSign(LessThanOrEqual):

    pass
class cobol_operators_LTEQPhrase(LessThanOrEqual):

    pass
class LessThan:

    pass
class cobol_operators_LTSign(LessThan):

    pass
class cobol_operators_LTPhrase(LessThan):

    pass
class operators_UnaryOperator:

    pass
class operators_AdditiveOperator:

    pass
class cobol_operators_Subtraction(operators_UnaryOperator, operators_AdditiveOperator):

    pass
class cobol_operators_Addition(operators_UnaryOperator, operators_AdditiveOperator):

    pass
class Operator:

    pass
class cobol_operators_MultiplicativeOperator(Operator):

    pass
class cobol_operators_Through(Operator):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_operators_SignOperator(Operator):

    pass
class cobol_operators_Power(Operator):

    pass
class cobol_operators_Negate(Operator):

    pass
class cobol_operators_UnaryOperator(Operator):

    pass
class cobol_operators_RelationalOperator(Operator):

    pass
class cobol_operators_ClassOperator(Operator):

    pass
class cobol_operators_LogicalOperator(Operator):

    pass
class cobol_operators_AdditiveOperator(Operator):

    pass
class cobol_operators_Operator(ABC):

    pass
class AlphanumericLiteral:

    pass
class cobol_literals_AlphanumericHexaDecimalLiteral(AlphanumericLiteral):

    pass
class DBCSLiteral:

    pass
class cobol_literals_NationalHexLiteral(DBCSLiteral):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class cobol_literals_NationalLiteral(DBCSLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ConstantLiteral:

    pass
class cobol_literals_Zero(ConstantLiteral):

    def __init__(self, value: str, ConstantLiteral: "cobol_literals_AllLiteral"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_literals_HighValue(ConstantLiteral):

    def __init__(self, value: str, ConstantLiteral: "cobol_literals_AllLiteral"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_literals_Null(ConstantLiteral):

    def __init__(self, value: str, ConstantLiteral: "cobol_literals_AllLiteral"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_literals_LowValue(ConstantLiteral):

    def __init__(self, value: str, ConstantLiteral: "cobol_literals_AllLiteral"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_literals_Space(ConstantLiteral):

    def __init__(self, value: str, ConstantLiteral: "cobol_literals_AllLiteral"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_literals_Quote(ConstantLiteral):

    def __init__(self, value: str, ConstantLiteral: "cobol_literals_AllLiteral"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class FigurativeConstantLiteral:

    pass
class cobol_literals_ConstantLiteral(FigurativeConstantLiteral):

    pass
class cobol_literals_AllLiteral(FigurativeConstantLiteral):

    pass
class DecimalLiteral:

    pass
class cobol_literals_FixedDecimalLiteral(DecimalLiteral):

    pass
class cobol_literals_FloatingDecimalLiteral(DecimalLiteral):

    pass
class NumericLiteral:

    pass
class cobol_literals_DecimalLiteral(NumericLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class water_IOControlParagraphWater:

    pass
class water_FileDescriptorWater:

    pass
class water_ObjectComputerParagraphWater:

    pass
class literals_NumericLiteral:

    pass
class cobol_literals_IntegerLiteral(literals_NumericLiteral, water_FileDescriptorWater, water_IOControlParagraphWater, water_ObjectComputerParagraphWater):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class Literal:

    pass
class cobol_literals_BooleanLiteral(Literal):

    def __init__(self, value: bool, Literal: "cobol_specialnames_CurrencySign"):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class cobol_literals_Any(Literal):

    pass
class cobol_literals_FigurativeConstantLiteral(Literal):

    pass
class cobol_literals_NumericLiteral(Literal):

    pass
class cobol_literals_PseudoLiteral(Literal):

    def __init__(self, value: str, Literal: "cobol_specialnames_CurrencySign"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cobol_literals_DBCSLiteral(Literal):

    pass
class cobol_literals_Characters(Literal):

    pass
class cobol_literals_AlphanumericLiteral(Literal):

    def __init__(self, value: str, Literal: "cobol_specialnames_CurrencySign"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class labels_StopLabel:

    pass
class water_InvokeStatementWater:

    pass
class operands_PrimaryOperand:

    pass
class water_CICSStatementWater:

    pass
class water_SpecialNamesParagraphWater:

    pass
class water_SelectStatementWater:

    pass
class cobol_identifiers_Identifier(water_AcceptStatementWater, water_SortPhraseWater, water_FileDescriptorWater, water_DataDescriptorWater, water_SQLStatementWater, water_UseStatementWater, water_RepositoryParagraphWater, water_InvokeStatementWater, water_ObjectComputerParagraphWater, water_IdentificationDivisionWater, water_CICSStatementWater, water_IOControlParagraphWater, water_SpecialNamesParagraphWater, operands_PrimaryOperand, water_SelectStatementWater):

    pass
class cobol_literals_Literal(water_InvokeStatementWater, labels_StopLabel, water_CICSStatementWater, water_SpecialNamesParagraphWater, operands_PrimaryOperand, water_SelectStatementWater):

    pass
class Declaratives:

    pass
class parameters_Parametrizable:

    pass
class cobol_statements_Entry(parameters_Parametrizable, statements_Statement):

    pass
class water_IncompleteElement:

    pass
class cobol_statements_Accept(water_IncompleteElement, statements_Statement):

    pass
class cobol_tables_Table(water_IncompleteElement, dataitems_DataItem):

    pass
class cobol_statements_Open(water_IncompleteElement, statements_IOStatement):

    pass
class cobol_files_FileName(water_IncompleteElement, references_ReferenceableElement):

    def __init__(self, fileDescriptor: str, cobol_files_FileName: set["DataItem"] = None, cobol_files_FileName362: set["DataItemAttribute"] = None, cobol_files_FileName365: set["StatementContainer"] = None):
        self.fileDescriptor = fileDescriptor
        self.cobol_files_FileName = cobol_files_FileName if cobol_files_FileName is not None else set()
        self.cobol_files_FileName362 = cobol_files_FileName362 if cobol_files_FileName362 is not None else set()
        self.cobol_files_FileName365 = cobol_files_FileName365 if cobol_files_FileName365 is not None else set()
        
    @property
    def fileDescriptor(self) -> str:
        return self.__fileDescriptor

    @fileDescriptor.setter
    def fileDescriptor(self, fileDescriptor: str):
        self.__fileDescriptor = fileDescriptor

    @property
    def cobol_files_FileName365(self):
        return self.__cobol_files_FileName365

    @cobol_files_FileName365.setter
    def cobol_files_FileName365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_files_FileName__cobol_files_FileName365", None)
        self.__cobol_files_FileName365 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StatementContainer366"):
                    opp_val = getattr(item, "StatementContainer366", None)
                    
                    if opp_val == self:
                        setattr(item, "StatementContainer366", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StatementContainer366"):
                    opp_val = getattr(item, "StatementContainer366", None)
                    
                    setattr(item, "StatementContainer366", self)
                    

    @property
    def cobol_files_FileName(self):
        return self.__cobol_files_FileName

    @cobol_files_FileName.setter
    def cobol_files_FileName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_files_FileName__cobol_files_FileName", None)
        self.__cobol_files_FileName = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataItem360"):
                    opp_val = getattr(item, "DataItem360", None)
                    
                    if opp_val == self:
                        setattr(item, "DataItem360", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataItem360"):
                    opp_val = getattr(item, "DataItem360", None)
                    
                    setattr(item, "DataItem360", self)
                    

    @property
    def cobol_files_FileName362(self):
        return self.__cobol_files_FileName362

    @cobol_files_FileName362.setter
    def cobol_files_FileName362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_files_FileName__cobol_files_FileName362", None)
        self.__cobol_files_FileName362 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataItemAttribute363"):
                    opp_val = getattr(item, "DataItemAttribute363", None)
                    
                    if opp_val == self:
                        setattr(item, "DataItemAttribute363", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataItemAttribute363"):
                    opp_val = getattr(item, "DataItemAttribute363", None)
                    
                    setattr(item, "DataItemAttribute363", self)
                    

class cobol_statements_Close(water_IncompleteElement, statements_IOStatement):

    pass
class cobol_sentences_UseSentence(water_IncompleteElement, sentences_StatementContainer):

    pass
class cobol_dataitems_DataItem(water_IncompleteElement, references_ReferenceableElement):

    def __init__(self, levelNumber: str, DataItem323: set["DataItem"] = None, DataItem325: "DataItem" = None, cobol_dataitems_DataItem: set["DataItemAttribute"] = None):
        self.levelNumber = levelNumber
        self.DataItem323 = DataItem323 if DataItem323 is not None else set()
        self.DataItem325 = DataItem325
        self.cobol_dataitems_DataItem = cobol_dataitems_DataItem if cobol_dataitems_DataItem is not None else set()
        
    @property
    def levelNumber(self) -> str:
        return self.__levelNumber

    @levelNumber.setter
    def levelNumber(self, levelNumber: str):
        self.__levelNumber = levelNumber

    @property
    def DataItem325(self):
        return self.__DataItem325

    @DataItem325.setter
    def DataItem325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_dataitems_DataItem__DataItem325", None)
        self.__DataItem325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataitems326"):
                opp_val = getattr(old_value, "dataitems326", None)
                if opp_val == self:
                    setattr(old_value, "dataitems326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataitems326"):
                opp_val = getattr(value, "dataitems326", None)
                setattr(value, "dataitems326", self)

    @property
    def DataItem323(self):
        return self.__DataItem323

    @DataItem323.setter
    def DataItem323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_dataitems_DataItem__DataItem323", None)
        self.__DataItem323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataitems"):
                    opp_val = getattr(item, "dataitems", None)
                    
                    if opp_val == self:
                        setattr(item, "dataitems", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataitems"):
                    opp_val = getattr(item, "dataitems", None)
                    
                    setattr(item, "dataitems", self)
                    

    @property
    def cobol_dataitems_DataItem(self):
        return self.__cobol_dataitems_DataItem

    @cobol_dataitems_DataItem.setter
    def cobol_dataitems_DataItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_dataitems_DataItem__cobol_dataitems_DataItem", None)
        self.__cobol_dataitems_DataItem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataItemAttribute"):
                    opp_val = getattr(item, "DataItemAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "DataItemAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataItemAttribute"):
                    opp_val = getattr(item, "DataItemAttribute", None)
                    
                    setattr(item, "DataItemAttribute", self)
                    

class cobol_paragraphs_IOControlParagraph(water_IncompleteElement, paragraphs_IOSectionParagraph):

    pass
class cobol_paragraphs_ObjectComputerParagraph(water_IncompleteElement, paragraphs_ConfigurationSectionParagraph):

    pass
class cobol_statements_Merge(water_IncompleteElement, statements_FileIOStatement):

    pass
class cobol_paragraphs_RepositoryParagraph(water_IncompleteElement, paragraphs_ConfigurationSectionParagraph):

    pass
class cobol_statements_Sort(water_IncompleteElement, statements_FileIOStatement):

    pass
class divisions_Division:

    pass
class cobol_divisions_ProcedureDivision(divisions_Division, parameters_Parametrizable):

    pass
class cobol_divisions_IdentificationDivision(water_IncompleteElement, divisions_Division):

    def __init__(self, properties: str):
        self.properties = properties
        
    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

class Division:

    pass
class cobol_divisions_EnvironmentDivision(Division):

    pass
class cobol_divisions_DataDivision(Division):

    pass
class StatementContainer:

    pass
class cobol_sentences_Sentence(StatementContainer):

    pass
class cobol_sentences_ExecuteSentence(StatementContainer):

    pass
class Paragraph:

    pass
class cobol_paragraphs_IOSectionParagraph(Paragraph):

    pass
class cobol_paragraphs_ConfigurationSectionParagraph(Paragraph):

    pass
class Section:

    pass
class cobol_sections_DataDivisionSection(Section):

    pass
class cobol_sections_EnvironmentDivisionSection(Section):

    pass
class cobol_sections_DeclarativeSection(Section):

    pass
class CobolRoot:

    pass
class cobol_containers_EmptyModel(CobolRoot):

    pass
class cobol_containers_CobolRoot(ABC):

    pass
class ProcedureDivision:

    pass
class DataDivision:

    pass
class EnvironmentDivision:

    pass
class IdentificationDivision:

    pass
class NamedElement:

    pass
class cobol_divisions_Division(NamedElement):

    pass
class cobol_references_ReferenceableElement(NamedElement):

    pass
class cobol_containers_CompilationUnit(NamedElement):

    pass
class CompilationUnit:

    pass
class commons_NamedElement:

    pass
class cobol_paragraphs_Paragraph(labels_Procedure, commons_NamedElement):

    pass
class cobol_sections_Section(labels_Procedure, commons_NamedElement):

    def __init__(self, segmentNumber: str, cobol_sections_Section: set["StatementContainer"] = None, cobol_sections_Section114: set["Paragraph"] = None):
        self.segmentNumber = segmentNumber
        self.cobol_sections_Section = cobol_sections_Section if cobol_sections_Section is not None else set()
        self.cobol_sections_Section114 = cobol_sections_Section114 if cobol_sections_Section114 is not None else set()
        
    @property
    def segmentNumber(self) -> str:
        return self.__segmentNumber

    @segmentNumber.setter
    def segmentNumber(self, segmentNumber: str):
        self.__segmentNumber = segmentNumber

    @property
    def cobol_sections_Section114(self):
        return self.__cobol_sections_Section114

    @cobol_sections_Section114.setter
    def cobol_sections_Section114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_sections_Section__cobol_sections_Section114", None)
        self.__cobol_sections_Section114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Paragraph115"):
                    opp_val = getattr(item, "Paragraph115", None)
                    
                    if opp_val == self:
                        setattr(item, "Paragraph115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Paragraph115"):
                    opp_val = getattr(item, "Paragraph115", None)
                    
                    setattr(item, "Paragraph115", self)
                    

    @property
    def cobol_sections_Section(self):
        return self.__cobol_sections_Section

    @cobol_sections_Section.setter
    def cobol_sections_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cobol_sections_Section__cobol_sections_Section", None)
        self.__cobol_sections_Section = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StatementContainer112"):
                    opp_val = getattr(item, "StatementContainer112", None)
                    
                    if opp_val == self:
                        setattr(item, "StatementContainer112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StatementContainer112"):
                    opp_val = getattr(item, "StatementContainer112", None)
                    
                    setattr(item, "StatementContainer112", self)
                    

class cobol_functions_FunctionCall(functions_Argumentable, commons_NamedElement, identifiers_Identifier):

    pass
class cobol_tables_IndexName(commons_NamedElement, references_ReferenceableElement):

    pass
class cobol_specialnames_ConditionName(specialnames_SpecialName, commons_NamedElement):

    pass
class containers_CobolRoot:

    pass
class cobol_containers_CompilationGroup(commons_NamedElement, containers_CobolRoot):

    pass
class conditions_SimpleConditionChild:

    pass
class conditions_AbbreviatedRelationalExpressionChild:

    pass
class cobol_arithmetics_ArithmeticExpression(conditions_SimpleConditionChild, conditions_AbbreviatedRelationalExpressionChild):

    pass
class PrimaryExpression:

    pass
class cobol_arithmetics_NestedArithmeticExpression(PrimaryExpression):

    pass
class RangeExpressionChild:

    pass
class cobol_arithmetics_AdditiveArithmeticExpression(RangeExpressionChild):

    pass
class Through:

    pass
class ArithmeticExpression:

    pass
class cobol_arithmetics_RangeExpressionChild(ArithmeticExpression):

    pass
class cobol_arithmetics_RangeExpression(ArithmeticExpression):

    pass
class Equal:

    pass
class cobol_operators_EqualPhrase(Equal):

    pass
class cobol_operators_EqualSign(Equal):

    pass
class cobol_arithmetics_AssignmentExpression:

    pass
class UnaryOperator:

    pass
class UnaryArithmeticExpressionChild:

    pass
class cobol_arithmetics_PrimaryExpression(UnaryArithmeticExpressionChild):

    pass
class PowerArithmeticExpressionChild:

    pass
class cobol_arithmetics_UnaryArithmeticExpression(PowerArithmeticExpressionChild):

    pass
class cobol_arithmetics_UnaryArithmeticExpressionChild(PowerArithmeticExpressionChild):

    pass
class MultiplicativeOperator:

    pass
class cobol_operators_Multiplication(MultiplicativeOperator):

    pass
class cobol_operators_Division(MultiplicativeOperator):

    pass
class MultiplicativeArithmeticExpressionChild:

    pass
class cobol_arithmetics_PowerArithmeticExpression(MultiplicativeArithmeticExpressionChild):

    pass
class cobol_arithmetics_PowerArithmeticExpressionChild(MultiplicativeArithmeticExpressionChild):

    pass
class cobol_arithmetics_AdditiveArithmeticExpressionChild(RangeExpressionChild):

    pass
class AdditiveOperator:

    pass
class AdditiveArithmeticExpressionChild:

    pass
class cobol_arithmetics_MultiplicativeArithmeticExpressionChild(AdditiveArithmeticExpressionChild):

    pass
class cobol_arithmetics_MultiplicativeArithmeticExpression(AdditiveArithmeticExpressionChild):

    pass
class NegatedAbbreviatedConditionalExpressionChild:

    pass
class cobol_conditions_AbbreviatedRelationalExpressionChild(NegatedAbbreviatedConditionalExpressionChild):

    pass
class ClassOperator:

    pass
class cobol_operators_Alphabetic(ClassOperator):

    pass
class cobol_operators_AlphabeticUpper(ClassOperator):

    pass
class cobol_operators_AlphabeticLower(ClassOperator):

    pass
class cobol_operators_ClassName(ClassOperator):

    pass
class cobol_operators_DBCS(ClassOperator):

    pass
class cobol_operators_Numeric(ClassOperator):

    pass
class cobol_operators_Kanji(ClassOperator):

    pass
class SignOperator:

    pass
class cobol_operators_Negative(SignOperator):

    pass
class cobol_operators_Zero(SignOperator):

    pass
class cobol_operators_Positive(SignOperator):

    pass
class AbbreviatedRelationalExpressionChild:

    pass
class cobol_conditions_NestedAbbreviatedConditionalExpression(AbbreviatedRelationalExpressionChild):

    pass
class cobol_conditions_AbbreviatedRelationalExpression(NegatedAbbreviatedConditionalExpressionChild):

    pass
class AbbreviatedConditionalExpressionChild:

    pass
class cobol_conditions_NegatedAbbreviatedConditionalExpression(AbbreviatedConditionalExpressionChild):

    pass
class cobol_conditions_NegatedAbbreviatedConditionalExpressionChild(AbbreviatedConditionalExpressionChild):

    pass
class cobol_conditions_ExpressionList:

    pass
class Is:

    pass
class RelationalOperator:

    pass
class cobol_operators_LessThan(RelationalOperator):

    def __init__(self, than: bool, RelationalOperator: "cobol_conditions_RelationalExpression", RelationalOperator288: "cobol_statements_Start", RelationalOperator22: "cobol_conditions_AbbreviatedRelationalExpression"):
        self.than = than
        
    @property
    def than(self) -> bool:
        return self.__than

    @than.setter
    def than(self, than: bool):
        self.__than = than

class cobol_operators_LessThanOrEqual(RelationalOperator):

    def __init__(self, than: bool, to: bool, RelationalOperator: "cobol_conditions_RelationalExpression", RelationalOperator288: "cobol_statements_Start", RelationalOperator22: "cobol_conditions_AbbreviatedRelationalExpression"):
        self.than = than
        self.to = to
        
    @property
    def than(self) -> bool:
        return self.__than

    @than.setter
    def than(self, than: bool):
        self.__than = than

    @property
    def to(self) -> bool:
        return self.__to

    @to.setter
    def to(self, to: bool):
        self.__to = to

class cobol_operators_GreaterThanOrEqual(RelationalOperator):

    def __init__(self, than: bool, to: bool, RelationalOperator: "cobol_conditions_RelationalExpression", RelationalOperator288: "cobol_statements_Start", RelationalOperator22: "cobol_conditions_AbbreviatedRelationalExpression"):
        self.than = than
        self.to = to
        
    @property
    def than(self) -> bool:
        return self.__than

    @than.setter
    def than(self, than: bool):
        self.__than = than

    @property
    def to(self) -> bool:
        return self.__to

    @to.setter
    def to(self, to: bool):
        self.__to = to

class cobol_operators_GreaterThan(RelationalOperator):

    def __init__(self, than: bool, RelationalOperator: "cobol_conditions_RelationalExpression", RelationalOperator288: "cobol_statements_Start", RelationalOperator22: "cobol_conditions_AbbreviatedRelationalExpression"):
        self.than = than
        
    @property
    def than(self) -> bool:
        return self.__than

    @than.setter
    def than(self, than: bool):
        self.__than = than

class cobol_operators_Equal(RelationalOperator):

    def __init__(self, to: bool, RelationalOperator: "cobol_conditions_RelationalExpression", RelationalOperator288: "cobol_statements_Start", RelationalOperator22: "cobol_conditions_AbbreviatedRelationalExpression"):
        self.to = to
        
    @property
    def to(self) -> bool:
        return self.__to

    @to.setter
    def to(self, to: bool):
        self.__to = to

class SimpleConditionChild:

    pass
class cobol_conditions_NestedCondition(SimpleConditionChild):

    pass
class Negate:

    pass
class NegatedConditionalExpressionChild:

    pass
class cobol_conditions_ClassCondition(NegatedConditionalExpressionChild):

    pass
class cobol_conditions_SimpleConditionChild(NegatedConditionalExpressionChild):

    pass
class cobol_conditions_RelationalExpression(NegatedConditionalExpressionChild):

    pass
class cobol_conditions_SignCondition(NegatedConditionalExpressionChild):

    pass
class ConditionalAndExpressionChild:

    pass
class cobol_conditions_NegatedConditionalExpressionChild(ConditionalAndExpressionChild):

    pass
class cobol_conditions_AbbreviatedConditionalExpressionChild(ConditionalAndExpressionChild):

    pass
class cobol_conditions_AbbreviatedConditionalExpression(ConditionalAndExpressionChild):

    pass
class cobol_conditions_NegatedConditionalExpression(ConditionalAndExpressionChild):

    pass
class LogicalOperator:

    pass
class cobol_operators_ConditionAnd(LogicalOperator):

    pass
class cobol_operators_ConditionOr(LogicalOperator):

    pass
class ConditionalOrExpressionChild:

    pass
class cobol_conditions_ConditionalAndExpressionChild(ConditionalOrExpressionChild):

    pass
class cobol_conditions_ConditionalAndExpression(ConditionalOrExpressionChild):

    pass
class Condition:

    pass
class cobol_conditions_ConditionalOrExpressionChild(Condition):

    pass
class cobol_conditions_ConditionalOrExpression(Condition):

    pass
class cobol_conditions_Condition(ABC):

    pass
class cobol_commons_Commentable(ABC):

    pass
class Commentable:

    pass
class cobol_commons_URIableElement(Commentable):

    def __init__(self, uri: str):
        self.uri = uri
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class cobol_commons_LabellableElement(Commentable):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class cobol_commons_NamedElement(Commentable):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
