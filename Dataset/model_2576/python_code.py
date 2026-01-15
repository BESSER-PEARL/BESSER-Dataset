from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RightAbsentSequenceSource:

    pass
class siddhi_RightAbsentSequenceSource1(RightAbsentSequenceSource):

    pass
class LeftAbsentSequenceSource:

    pass
class siddhi_LeftAbsentSequenceSource1(LeftAbsentSequenceSource):

    pass
class siddhi_TRUE:

    def __init__(self, tr: str):
        self.tr = tr
        
    @property
    def tr(self) -> str:
        return self.__tr

    @tr.setter
    def tr(self, tr: str):
        self.__tr = tr

class siddhi_FALSE:

    def __init__(self, fals: str):
        self.fals = fals
        
    @property
    def fals(self) -> str:
        return self.__fals

    @fals.setter
    def fals(self, fals: str):
        self.__fals = fals

class siddhi_MILLISECONDS:

    def __init__(self, millisecond: str, milliseconds: str, millisec: str):
        self.millisecond = millisecond
        self.milliseconds = milliseconds
        self.millisec = millisec
        
    @property
    def millisec(self) -> str:
        return self.__millisec

    @millisec.setter
    def millisec(self, millisec: str):
        self.__millisec = millisec

    @property
    def milliseconds(self) -> str:
        return self.__milliseconds

    @milliseconds.setter
    def milliseconds(self, milliseconds: str):
        self.__milliseconds = milliseconds

    @property
    def millisecond(self) -> str:
        return self.__millisecond

    @millisecond.setter
    def millisecond(self, millisecond: str):
        self.__millisecond = millisecond

class siddhi_SECONDS:

    def __init__(self, seconds: str, second: str, sec: str):
        self.seconds = seconds
        self.second = second
        self.sec = sec
        
    @property
    def second(self) -> str:
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second

    @property
    def seconds(self) -> str:
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: str):
        self.__seconds = seconds

    @property
    def sec(self) -> str:
        return self.__sec

    @sec.setter
    def sec(self, sec: str):
        self.__sec = sec

class siddhi_MINUTES:

    def __init__(self, minute: str, minutes: str, min: str):
        self.minute = minute
        self.minutes = minutes
        self.min = min
        
    @property
    def minutes(self) -> str:
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: str):
        self.__minutes = minutes

    @property
    def minute(self) -> str:
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

class siddhi_HOURS:

    def __init__(self, hour: str, hours: str):
        self.hour = hour
        self.hours = hours
        
    @property
    def hours(self) -> str:
        return self.__hours

    @hours.setter
    def hours(self, hours: str):
        self.__hours = hours

    @property
    def hour(self) -> str:
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour

class siddhi_DAYS:

    def __init__(self, day: str, days: str):
        self.day = day
        self.days = days
        
    @property
    def days(self) -> str:
        return self.__days

    @days.setter
    def days(self, days: str):
        self.__days = days

    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

class siddhi_MONTHS:

    def __init__(self, month: str, months: str):
        self.month = month
        self.months = months
        
    @property
    def months(self) -> str:
        return self.__months

    @months.setter
    def months(self, months: str):
        self.__months = months

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

class siddhi_YEARS:

    def __init__(self, year: str, years: str):
        self.year = year
        self.years = years
        
    @property
    def years(self) -> str:
        return self.__years

    @years.setter
    def years(self, years: str):
        self.__years = years

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

class siddhi_PER:

    def __init__(self, per: str):
        self.per = per
        
    @property
    def per(self) -> str:
        return self.__per

    @per.setter
    def per(self, per: str):
        self.__per = per

class siddhi_SET:

    def __init__(self, set: str):
        self.set = set
        
    @property
    def set(self) -> str:
        return self.__set

    @set.setter
    def set(self, set: str):
        self.__set = set

class siddhi_AGGREGATE:

    def __init__(self, agrregate: str):
        self.agrregate = agrregate
        
    @property
    def agrregate(self) -> str:
        return self.__agrregate

    @agrregate.setter
    def agrregate(self, agrregate: str):
        self.__agrregate = agrregate

class siddhi_AGGREGATION:

    def __init__(self, aggre: str):
        self.aggre = aggre
        
    @property
    def aggre(self) -> str:
        return self.__aggre

    @aggre.setter
    def aggre(self, aggre: str):
        self.__aggre = aggre

class siddhi_WITH:

    def __init__(self, wi: str):
        self.wi = wi
        
    @property
    def wi(self) -> str:
        return self.__wi

    @wi.setter
    def wi(self, wi: str):
        self.__wi = wi

class siddhi_PARTITION:

    def __init__(self, partition: str):
        self.partition = partition
        
    @property
    def partition(self) -> str:
        return self.__partition

    @partition.setter
    def partition(self, partition: str):
        self.__partition = partition

class siddhi_END:

    def __init__(self, end: str):
        self.end = end
        
    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

class siddhi_UPDATE:

    def __init__(self, update: str):
        self.update = update
        
    @property
    def update(self) -> str:
        return self.__update

    @update.setter
    def update(self, update: str):
        self.__update = update

class siddhi_FOR:

    def __init__(self, for: str):
        self.for = for
        
    @property
    def for(self) -> str:
        return self.__for

    @for.setter
    def for(self, for: str):
        self.__for = for

class siddhi_DELETE:

    def __init__(self, delete: str):
        self.delete = delete
        
    @property
    def delete(self) -> str:
        return self.__delete

    @delete.setter
    def delete(self, delete: str):
        self.__delete = delete

class siddhi_PLAN:

    def __init__(self, plan: str):
        self.plan = plan
        
    @property
    def plan(self) -> str:
        return self.__plan

    @plan.setter
    def plan(self, plan: str):
        self.__plan = plan

class siddhi_BEGIN:

    def __init__(self, begin: str):
        self.begin = begin
        
    @property
    def begin(self) -> str:
        return self.__begin

    @begin.setter
    def begin(self, begin: str):
        self.__begin = begin

class siddhi_WEEKS:

    def __init__(self, week: str, weeks: str):
        self.week = week
        self.weeks = weeks
        
    @property
    def weeks(self) -> str:
        return self.__weeks

    @weeks.setter
    def weeks(self, weeks: str):
        self.__weeks = weeks

    @property
    def week(self) -> str:
        return self.__week

    @week.setter
    def week(self, week: str):
        self.__week = week

class siddhi_FUNCTION:

    def __init__(self, function: str):
        self.function = function
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

class siddhi_INSERT:

    def __init__(self, insert: str):
        self.insert = insert
        
    @property
    def insert(self) -> str:
        return self.__insert

    @insert.setter
    def insert(self, insert: str):
        self.__insert = insert

class siddhi_FIRST:

    def __init__(self, first: str):
        self.first = first
        
    @property
    def first(self) -> str:
        return self.__first

    @first.setter
    def first(self, first: str):
        self.__first = first

class siddhi_AT:

    def __init__(self, at: str):
        self.at = at
        
    @property
    def at(self) -> str:
        return self.__at

    @at.setter
    def at(self, at: str):
        self.__at = at

class siddhi_SNAPSHOT:

    def __init__(self, snapshot: str):
        self.snapshot = snapshot
        
    @property
    def snapshot(self) -> str:
        return self.__snapshot

    @snapshot.setter
    def snapshot(self, snapshot: str):
        self.__snapshot = snapshot

class siddhi_TRIGGER:

    def __init__(self, trigger: str):
        self.trigger = trigger
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

class siddhi_HAVING:

    def __init__(self, having: str):
        self.having = having
        
    @property
    def having(self) -> str:
        return self.__having

    @having.setter
    def having(self, having: str):
        self.__having = having

class siddhi_NULL:

    def __init__(self, null: str):
        self.null = null
        
    @property
    def null(self) -> str:
        return self.__null

    @null.setter
    def null(self, null: str):
        self.__null = null

class siddhi_BY:

    def __init__(self, by: str):
        self.by = by
        
    @property
    def by(self) -> str:
        return self.__by

    @by.setter
    def by(self, by: str):
        self.__by = by

class siddhi_IS:

    def __init__(self, is: str):
        self.is = is
        
    @property
    def is(self) -> str:
        return self.__is

    @is.setter
    def is(self, is: str):
        self.__is = is

class siddhi_GROUP:

    def __init__(self, group: str):
        self.group = group
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

class siddhi_LAST:

    def __init__(self, last: str):
        self.last = last
        
    @property
    def last(self) -> str:
        return self.__last

    @last.setter
    def last(self, last: str):
        self.__last = last

class siddhi_SELECT:

    def __init__(self, select: str):
        self.select = select
        
    @property
    def select(self) -> str:
        return self.__select

    @select.setter
    def select(self, select: str):
        self.__select = select

class siddhi_CURRENT:

    def __init__(self, currt: str):
        self.currt = currt
        
    @property
    def currt(self) -> str:
        return self.__currt

    @currt.setter
    def currt(self, currt: str):
        self.__currt = currt

class siddhi_OUTER:

    def __init__(self, outer: str):
        self.outer = outer
        
    @property
    def outer(self) -> str:
        return self.__outer

    @outer.setter
    def outer(self, outer: str):
        self.__outer = outer

class siddhi_INNER:

    def __init__(self, inner: str):
        self.inner = inner
        
    @property
    def inner(self) -> str:
        return self.__inner

    @inner.setter
    def inner(self, inner: str):
        self.__inner = inner

class siddhi_JOIN:

    def __init__(self, join: str):
        self.join = join
        
    @property
    def join(self) -> str:
        return self.__join

    @join.setter
    def join(self, join: str):
        self.__join = join

class siddhi_FULL:

    def __init__(self, full: str):
        self.full = full
        
    @property
    def full(self) -> str:
        return self.__full

    @full.setter
    def full(self, full: str):
        self.__full = full

class siddhi_RIGHT:

    def __init__(self, right: str):
        self.right = right
        
    @property
    def right(self) -> str:
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right

class siddhi_LEFT:

    def __init__(self, left: str):
        self.left = left
        
    @property
    def left(self) -> str:
        return self.__left

    @left.setter
    def left(self, left: str):
        self.__left = left

class siddhi_WITHIN:

    def __init__(self, within: str):
        self.within = within
        
    @property
    def within(self) -> str:
        return self.__within

    @within.setter
    def within(self, within: str):
        self.__within = within

class siddhi_FROM:

    def __init__(self, from: str):
        self.from = from
        
    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

class siddhi_RETURN:

    def __init__(self, return: str):
        self.return = return
        
    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

class siddhi_INTO:

    def __init__(self, into: str):
        self.into = into
        
    @property
    def into(self) -> str:
        return self.__into

    @into.setter
    def into(self, into: str):
        self.__into = into

class siddhi_INTS:

    def __init__(self, int: str):
        self.int = int
        
    @property
    def int(self) -> str:
        return self.__int

    @int.setter
    def int(self, int: str):
        self.__int = int

class siddhi_STRINGS:

    def __init__(self, string: str):
        self.string = string
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

class siddhi_OUTPUT:

    def __init__(self, output: str):
        self.output = output
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

class siddhi_EXPIRED:

    def __init__(self, expired: str):
        self.expired = expired
        
    @property
    def expired(self) -> str:
        return self.__expired

    @expired.setter
    def expired(self, expired: str):
        self.__expired = expired

class siddhi_RAW:

    def __init__(self, raw: str):
        self.raw = raw
        
    @property
    def raw(self) -> str:
        return self.__raw

    @raw.setter
    def raw(self, raw: str):
        self.__raw = raw

class siddhi_EVENTS:

    def __init__(self, events: str):
        self.events = events
        
    @property
    def events(self) -> str:
        return self.__events

    @events.setter
    def events(self, events: str):
        self.__events = events

class siddhi_ALL:

    def __init__(self, all: str):
        self.all = all
        
    @property
    def all(self) -> str:
        return self.__all

    @all.setter
    def all(self, all: str):
        self.__all = all

class siddhi_OBJECT:

    def __init__(self, object: str):
        self.object = object
        
    @property
    def object(self) -> str:
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object

class siddhi_BOOL:

    def __init__(self, bool: str):
        self.bool = bool
        
    @property
    def bool(self) -> str:
        return self.__bool

    @bool.setter
    def bool(self, bool: str):
        self.__bool = bool

class siddhi_FLOAT:

    def __init__(self, float: str):
        self.float = float
        
    @property
    def float(self) -> str:
        return self.__float

    @float.setter
    def float(self, float: str):
        self.__float = float

class siddhi_DOUBLE:

    def __init__(self, double: str):
        self.double = double
        
    @property
    def double(self) -> str:
        return self.__double

    @double.setter
    def double(self, double: str):
        self.__double = double

class siddhi_LONG:

    def __init__(self, long: str):
        self.long = long
        
    @property
    def long(self) -> str:
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long

class siddhi_IN:

    def __init__(self, in: str, siddhi_IN: "siddhi_MathInOperation" = None):
        self.in = in
        self.siddhi_IN = siddhi_IN
        
    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

    @property
    def siddhi_IN(self):
        return self.__siddhi_IN

    @siddhi_IN.setter
    def siddhi_IN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_IN__siddhi_IN", None)
        self.__siddhi_IN = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathInOperation"):
                opp_val = getattr(old_value, "siddhi_MathInOperation", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathInOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathInOperation"):
                opp_val = getattr(value, "siddhi_MathInOperation", None)
                setattr(value, "siddhi_MathInOperation", self)

class RightAbsentPatternSource:

    pass
class siddhi_RightAbsentPatternSource1(RightAbsentPatternSource):

    def __init__(self, fb: str, siddhi_RightAbsentPatternSource1: "siddhi_RightAbsentPatternSource" = None, siddhi_RightAbsentPatternSource1653: "siddhi_EveryAbsentPatternSource" = None):
        self.fb = fb
        self.siddhi_RightAbsentPatternSource1 = siddhi_RightAbsentPatternSource1
        self.siddhi_RightAbsentPatternSource1653 = siddhi_RightAbsentPatternSource1653
        
    @property
    def fb(self) -> str:
        return self.__fb

    @fb.setter
    def fb(self, fb: str):
        self.__fb = fb

    @property
    def siddhi_RightAbsentPatternSource1(self):
        return self.__siddhi_RightAbsentPatternSource1

    @siddhi_RightAbsentPatternSource1.setter
    def siddhi_RightAbsentPatternSource1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource1__siddhi_RightAbsentPatternSource1", None)
        self.__siddhi_RightAbsentPatternSource1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource651"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource651", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource651", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource651"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource651", None)
                setattr(value, "siddhi_RightAbsentPatternSource651", self)

    @property
    def siddhi_RightAbsentPatternSource1653(self):
        return self.__siddhi_RightAbsentPatternSource1653

    @siddhi_RightAbsentPatternSource1653.setter
    def siddhi_RightAbsentPatternSource1653(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource1__siddhi_RightAbsentPatternSource1653", None)
        self.__siddhi_RightAbsentPatternSource1653 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryAbsentPatternSource654"):
                opp_val = getattr(old_value, "siddhi_EveryAbsentPatternSource654", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryAbsentPatternSource654", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryAbsentPatternSource654"):
                opp_val = getattr(value, "siddhi_EveryAbsentPatternSource654", None)
                setattr(value, "siddhi_EveryAbsentPatternSource654", self)

class LeftAbsentPatternSource:

    pass
class siddhi_LeftAbsentPatternSource1(LeftAbsentPatternSource):

    def __init__(self, fb: str):
        self.fb = fb
        
    @property
    def fb(self) -> str:
        return self.__fb

    @fb.setter
    def fb(self, fb: str):
        self.__fb = fb

class EveryAbsentPatternSource:

    pass
class EveryAbsentSequenceSourceChain:

    pass
class EverySequenceSourceChain:

    pass
class siddhi_WINDOW:

    def __init__(self, window: str):
        self.window = window
        
    @property
    def window(self) -> str:
        return self.__window

    @window.setter
    def window(self, window: str):
        self.__window = window

class siddhi_TABLE:

    def __init__(self, table: str):
        self.table = table
        
    @property
    def table(self) -> str:
        return self.__table

    @table.setter
    def table(self, table: str):
        self.__table = table

class siddhi_DEFINE:

    def __init__(self, define: str):
        self.define = define
        
    @property
    def define(self) -> str:
        return self.__define

    @define.setter
    def define(self, define: str):
        self.__define = define

class siddhi_STREAM:

    def __init__(self, str: str):
        self.str = str
        
    @property
    def str(self) -> str:
        return self.__str

    @str.setter
    def str(self, str: str):
        self.__str = str

class BasicAbsentPatternSource:

    pass
class LogicalAbsentStatefulSource:

    pass
class AppAnnotation:

    pass
class siddhi_APP(AppAnnotation):

    def __init__(self, ap: str, siddhi_APP: "siddhi_Name" = None, siddhi_APP643: set["siddhi_AnnotationElement"] = None):
        self.ap = ap
        self.siddhi_APP = siddhi_APP
        self.siddhi_APP643 = siddhi_APP643 if siddhi_APP643 is not None else set()
        
    @property
    def ap(self) -> str:
        return self.__ap

    @ap.setter
    def ap(self, ap: str):
        self.__ap = ap

    @property
    def siddhi_APP643(self):
        return self.__siddhi_APP643

    @siddhi_APP643.setter
    def siddhi_APP643(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_APP__siddhi_APP643", None)
        self.__siddhi_APP643 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "siddhi_AnnotationElement644"):
                    opp_val = getattr(item, "siddhi_AnnotationElement644", None)
                    
                    if opp_val == self:
                        setattr(item, "siddhi_AnnotationElement644", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "siddhi_AnnotationElement644"):
                    opp_val = getattr(item, "siddhi_AnnotationElement644", None)
                    
                    setattr(item, "siddhi_AnnotationElement644", self)
                    

    @property
    def siddhi_APP(self):
        return self.__siddhi_APP

    @siddhi_APP.setter
    def siddhi_APP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_APP__siddhi_APP", None)
        self.__siddhi_APP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Name641"):
                opp_val = getattr(old_value, "siddhi_Name641", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Name641", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Name641"):
                opp_val = getattr(value, "siddhi_Name641", None)
                setattr(value, "siddhi_Name641", self)

class Name:

    pass
class siddhi_L:

    def __init__(self, l: str, siddhi_L: "siddhi_LONG_LITERAL" = None):
        self.l = l
        self.siddhi_L = siddhi_L
        
    @property
    def l(self) -> str:
        return self.__l

    @l.setter
    def l(self, l: str):
        self.__l = l

    @property
    def siddhi_L(self):
        return self.__siddhi_L

    @siddhi_L.setter
    def siddhi_L(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_L__siddhi_L", None)
        self.__siddhi_L = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LONG_LITERAL"):
                opp_val = getattr(old_value, "siddhi_LONG_LITERAL", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LONG_LITERAL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LONG_LITERAL"):
                opp_val = getattr(value, "siddhi_LONG_LITERAL", None)
                setattr(value, "siddhi_LONG_LITERAL", self)

class SignedLongValue:

    pass
class siddhi_LONG_LITERAL(SignedLongValue):

    pass
class siddhi_F:

    def __init__(self, f: str, siddhi_F: "siddhi_FLOAT_LITERAL" = None):
        self.f = f
        self.siddhi_F = siddhi_F
        
    @property
    def f(self) -> str:
        return self.__f

    @f.setter
    def f(self, f: str):
        self.__f = f

    @property
    def siddhi_F(self):
        return self.__siddhi_F

    @siddhi_F.setter
    def siddhi_F(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_F__siddhi_F", None)
        self.__siddhi_F = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_FLOAT_LITERAL609"):
                opp_val = getattr(old_value, "siddhi_FLOAT_LITERAL609", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_FLOAT_LITERAL609", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_FLOAT_LITERAL609"):
                opp_val = getattr(value, "siddhi_FLOAT_LITERAL609", None)
                setattr(value, "siddhi_FLOAT_LITERAL609", self)

class SignedFloatValue:

    pass
class siddhi_FLOAT_LITERAL(SignedFloatValue):

    pass
class siddhi_D:

    def __init__(self, d: str, siddhi_D: "siddhi_DOUBLE_LITERAL" = None):
        self.d = d
        self.siddhi_D = siddhi_D
        
    @property
    def d(self) -> str:
        return self.__d

    @d.setter
    def d(self, d: str):
        self.__d = d

    @property
    def siddhi_D(self):
        return self.__siddhi_D

    @siddhi_D.setter
    def siddhi_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_D__siddhi_D", None)
        self.__siddhi_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DOUBLE_LITERAL605"):
                opp_val = getattr(old_value, "siddhi_DOUBLE_LITERAL605", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DOUBLE_LITERAL605", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DOUBLE_LITERAL605"):
                opp_val = getattr(value, "siddhi_DOUBLE_LITERAL605", None)
                setattr(value, "siddhi_DOUBLE_LITERAL605", self)

class siddhi_E:

    def __init__(self, e: str, siddhi_E: "siddhi_DOUBLE_LITERAL" = None, siddhi_E607: "siddhi_FLOAT_LITERAL" = None):
        self.e = e
        self.siddhi_E = siddhi_E
        self.siddhi_E607 = siddhi_E607
        
    @property
    def e(self) -> str:
        return self.__e

    @e.setter
    def e(self, e: str):
        self.__e = e

    @property
    def siddhi_E(self):
        return self.__siddhi_E

    @siddhi_E.setter
    def siddhi_E(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_E__siddhi_E", None)
        self.__siddhi_E = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DOUBLE_LITERAL"):
                opp_val = getattr(old_value, "siddhi_DOUBLE_LITERAL", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DOUBLE_LITERAL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DOUBLE_LITERAL"):
                opp_val = getattr(value, "siddhi_DOUBLE_LITERAL", None)
                setattr(value, "siddhi_DOUBLE_LITERAL", self)

    @property
    def siddhi_E607(self):
        return self.__siddhi_E607

    @siddhi_E607.setter
    def siddhi_E607(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_E__siddhi_E607", None)
        self.__siddhi_E607 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_FLOAT_LITERAL"):
                opp_val = getattr(old_value, "siddhi_FLOAT_LITERAL", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_FLOAT_LITERAL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_FLOAT_LITERAL"):
                opp_val = getattr(value, "siddhi_FLOAT_LITERAL", None)
                setattr(value, "siddhi_FLOAT_LITERAL", self)

class SignedDoubleValue:

    pass
class siddhi_DOUBLE_LITERAL(SignedDoubleValue):

    pass
class MILLISECONDS:

    pass
class siddhi_MillisecondValue(MILLISECONDS):

    pass
class FALSE:

    pass
class TRUE:

    pass
class siddhi_AttributeList:

    pass
class siddhi_FunctionId:

    pass
class siddhi_FunctionNamespace:

    pass
class siddhi_SignedLongValue:

    pass
class siddhi_SignedFloatValue:

    pass
class siddhi_SignedDoubleValue:

    pass
class siddhi_BoolValue(TRUE, FALSE):

    pass
class siddhi_AttributeNameReference:

    pass
class siddhi_Source1OrStandardStatefulSource:

    def __init__(self, name: str, siddhi_Source1OrStandardStatefulSource: "siddhi_SourceOrEventReference" = None):
        self.name = name
        self.siddhi_Source1OrStandardStatefulSource = siddhi_Source1OrStandardStatefulSource
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def siddhi_Source1OrStandardStatefulSource(self):
        return self.__siddhi_Source1OrStandardStatefulSource

    @siddhi_Source1OrStandardStatefulSource.setter
    def siddhi_Source1OrStandardStatefulSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Source1OrStandardStatefulSource__siddhi_Source1OrStandardStatefulSource", None)
        self.__siddhi_Source1OrStandardStatefulSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SourceOrEventReference549"):
                opp_val = getattr(old_value, "siddhi_SourceOrEventReference549", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SourceOrEventReference549", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SourceOrEventReference549"):
                opp_val = getattr(value, "siddhi_SourceOrEventReference549", None)
                setattr(value, "siddhi_SourceOrEventReference549", self)

class PatternCollectionStatefulSource:

    pass
class SequenceCollectionStatefulSource:

    pass
class siddhi_FeaturesOrOutAttr:

    def __init__(self, name: str, siddhi_FeaturesOrOutAttr: "siddhi_FeaturesOrOutAttrReference" = None):
        self.name = name
        self.siddhi_FeaturesOrOutAttr = siddhi_FeaturesOrOutAttr
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def siddhi_FeaturesOrOutAttr(self):
        return self.__siddhi_FeaturesOrOutAttr

    @siddhi_FeaturesOrOutAttr.setter
    def siddhi_FeaturesOrOutAttr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_FeaturesOrOutAttr__siddhi_FeaturesOrOutAttr", None)
        self.__siddhi_FeaturesOrOutAttr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_FeaturesOrOutAttrReference533"):
                opp_val = getattr(old_value, "siddhi_FeaturesOrOutAttrReference533", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_FeaturesOrOutAttrReference533", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_FeaturesOrOutAttrReference533"):
                opp_val = getattr(value, "siddhi_FeaturesOrOutAttrReference533", None)
                setattr(value, "siddhi_FeaturesOrOutAttrReference533", self)

class siddhi_FeaturesOrOutAttrReference:

    pass
class siddhi_SourceOrEventReference:

    pass
class SetAssignment:

    pass
class siddhi_ConstantValue:

    def __init__(self, siv: str, siddhi_ConstantValue: "siddhi_Literal" = None, siddhi_ConstantValue553: "siddhi_BoolValue" = None, siddhi_ConstantValue555: "siddhi_SignedDoubleValue" = None, siddhi_ConstantValue557: "siddhi_SignedFloatValue" = None, siddhi_ConstantValue559: "siddhi_SignedLongValue" = None, siddhi_ConstantValue561: "siddhi_TimeValue" = None, siddhi_ConstantValue564: "siddhi_StringValue" = None):
        self.siv = siv
        self.siddhi_ConstantValue = siddhi_ConstantValue
        self.siddhi_ConstantValue553 = siddhi_ConstantValue553
        self.siddhi_ConstantValue555 = siddhi_ConstantValue555
        self.siddhi_ConstantValue557 = siddhi_ConstantValue557
        self.siddhi_ConstantValue559 = siddhi_ConstantValue559
        self.siddhi_ConstantValue561 = siddhi_ConstantValue561
        self.siddhi_ConstantValue564 = siddhi_ConstantValue564
        
    @property
    def siv(self) -> str:
        return self.__siv

    @siv.setter
    def siv(self, siv: str):
        self.__siv = siv

    @property
    def siddhi_ConstantValue553(self):
        return self.__siddhi_ConstantValue553

    @siddhi_ConstantValue553.setter
    def siddhi_ConstantValue553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ConstantValue__siddhi_ConstantValue553", None)
        self.__siddhi_ConstantValue553 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_BoolValue"):
                opp_val = getattr(old_value, "siddhi_BoolValue", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_BoolValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_BoolValue"):
                opp_val = getattr(value, "siddhi_BoolValue", None)
                setattr(value, "siddhi_BoolValue", self)

    @property
    def siddhi_ConstantValue559(self):
        return self.__siddhi_ConstantValue559

    @siddhi_ConstantValue559.setter
    def siddhi_ConstantValue559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ConstantValue__siddhi_ConstantValue559", None)
        self.__siddhi_ConstantValue559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SignedLongValue"):
                opp_val = getattr(old_value, "siddhi_SignedLongValue", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SignedLongValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SignedLongValue"):
                opp_val = getattr(value, "siddhi_SignedLongValue", None)
                setattr(value, "siddhi_SignedLongValue", self)

    @property
    def siddhi_ConstantValue564(self):
        return self.__siddhi_ConstantValue564

    @siddhi_ConstantValue564.setter
    def siddhi_ConstantValue564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ConstantValue__siddhi_ConstantValue564", None)
        self.__siddhi_ConstantValue564 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_StringValue565"):
                opp_val = getattr(old_value, "siddhi_StringValue565", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_StringValue565", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_StringValue565"):
                opp_val = getattr(value, "siddhi_StringValue565", None)
                setattr(value, "siddhi_StringValue565", self)

    @property
    def siddhi_ConstantValue561(self):
        return self.__siddhi_ConstantValue561

    @siddhi_ConstantValue561.setter
    def siddhi_ConstantValue561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ConstantValue__siddhi_ConstantValue561", None)
        self.__siddhi_ConstantValue561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_TimeValue562"):
                opp_val = getattr(old_value, "siddhi_TimeValue562", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_TimeValue562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_TimeValue562"):
                opp_val = getattr(value, "siddhi_TimeValue562", None)
                setattr(value, "siddhi_TimeValue562", self)

    @property
    def siddhi_ConstantValue557(self):
        return self.__siddhi_ConstantValue557

    @siddhi_ConstantValue557.setter
    def siddhi_ConstantValue557(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ConstantValue__siddhi_ConstantValue557", None)
        self.__siddhi_ConstantValue557 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SignedFloatValue"):
                opp_val = getattr(old_value, "siddhi_SignedFloatValue", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SignedFloatValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SignedFloatValue"):
                opp_val = getattr(value, "siddhi_SignedFloatValue", None)
                setattr(value, "siddhi_SignedFloatValue", self)

    @property
    def siddhi_ConstantValue555(self):
        return self.__siddhi_ConstantValue555

    @siddhi_ConstantValue555.setter
    def siddhi_ConstantValue555(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ConstantValue__siddhi_ConstantValue555", None)
        self.__siddhi_ConstantValue555 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SignedDoubleValue"):
                opp_val = getattr(old_value, "siddhi_SignedDoubleValue", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SignedDoubleValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SignedDoubleValue"):
                opp_val = getattr(value, "siddhi_SignedDoubleValue", None)
                setattr(value, "siddhi_SignedDoubleValue", self)

    @property
    def siddhi_ConstantValue(self):
        return self.__siddhi_ConstantValue

    @siddhi_ConstantValue.setter
    def siddhi_ConstantValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ConstantValue__siddhi_ConstantValue", None)
        self.__siddhi_ConstantValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Literal509"):
                opp_val = getattr(old_value, "siddhi_Literal509", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Literal509", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Literal509"):
                opp_val = getattr(value, "siddhi_Literal509", None)
                setattr(value, "siddhi_Literal509", self)

class siddhi_StreamReference:

    def __init__(self, hash: str, siddhi_StreamReference: "siddhi_NullCheck" = None, siddhi_StreamReference504: "siddhi_Name" = None, siddhi_StreamReference507: "siddhi_AttributeIndex" = None):
        self.hash = hash
        self.siddhi_StreamReference = siddhi_StreamReference
        self.siddhi_StreamReference504 = siddhi_StreamReference504
        self.siddhi_StreamReference507 = siddhi_StreamReference507
        
    @property
    def hash(self) -> str:
        return self.__hash

    @hash.setter
    def hash(self, hash: str):
        self.__hash = hash

    @property
    def siddhi_StreamReference504(self):
        return self.__siddhi_StreamReference504

    @siddhi_StreamReference504.setter
    def siddhi_StreamReference504(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StreamReference__siddhi_StreamReference504", None)
        self.__siddhi_StreamReference504 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Name505"):
                opp_val = getattr(old_value, "siddhi_Name505", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Name505", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Name505"):
                opp_val = getattr(value, "siddhi_Name505", None)
                setattr(value, "siddhi_Name505", self)

    @property
    def siddhi_StreamReference(self):
        return self.__siddhi_StreamReference

    @siddhi_StreamReference.setter
    def siddhi_StreamReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StreamReference__siddhi_StreamReference", None)
        self.__siddhi_StreamReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_NullCheck"):
                opp_val = getattr(old_value, "siddhi_NullCheck", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_NullCheck", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_NullCheck"):
                opp_val = getattr(value, "siddhi_NullCheck", None)
                setattr(value, "siddhi_NullCheck", self)

    @property
    def siddhi_StreamReference507(self):
        return self.__siddhi_StreamReference507

    @siddhi_StreamReference507.setter
    def siddhi_StreamReference507(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StreamReference__siddhi_StreamReference507", None)
        self.__siddhi_StreamReference507 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_AttributeIndex"):
                opp_val = getattr(old_value, "siddhi_AttributeIndex", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_AttributeIndex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_AttributeIndex"):
                opp_val = getattr(value, "siddhi_AttributeIndex", None)
                setattr(value, "siddhi_AttributeIndex", self)

class NULL:

    pass
class IS:

    pass
class MathOtherOperations:

    pass
class siddhi_NotOperation(MathOtherOperations):

    pass
class siddhi_NullCheck(MathOtherOperations, NULL, IS):

    pass
class siddhi_Literal:

    pass
class MathDivmulOperation:

    pass
class siddhi_MathOtherOperations(MathDivmulOperation):

    pass
class MathAddsubOperation:

    pass
class siddhi_MathDivmulOperation(MathAddsubOperation):

    def __init__(self, multiply: str, devide: str, mod: str, siddhi_MathDivmulOperation: "siddhi_MathAddsubOperation" = None):
        self.multiply = multiply
        self.devide = devide
        self.mod = mod
        self.siddhi_MathDivmulOperation = siddhi_MathDivmulOperation
        
    @property
    def mod(self) -> str:
        return self.__mod

    @mod.setter
    def mod(self, mod: str):
        self.__mod = mod

    @property
    def multiply(self) -> str:
        return self.__multiply

    @multiply.setter
    def multiply(self, multiply: str):
        self.__multiply = multiply

    @property
    def devide(self) -> str:
        return self.__devide

    @devide.setter
    def devide(self, devide: str):
        self.__devide = devide

    @property
    def siddhi_MathDivmulOperation(self):
        return self.__siddhi_MathDivmulOperation

    @siddhi_MathDivmulOperation.setter
    def siddhi_MathDivmulOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_MathDivmulOperation__siddhi_MathDivmulOperation", None)
        self.__siddhi_MathDivmulOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathAddsubOperation"):
                opp_val = getattr(old_value, "siddhi_MathAddsubOperation", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathAddsubOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathAddsubOperation"):
                opp_val = getattr(value, "siddhi_MathAddsubOperation", None)
                setattr(value, "siddhi_MathAddsubOperation", self)

class MathOperation:

    pass
class siddhi_MathInOperation(MathOperation):

    pass
class siddhi_MathLogicalOperation(MathOperation):

    pass
class siddhi_MathGtLtOperation(MathOperation):

    def __init__(self, gt_eq: str, lt_eq: str, gt: str, lt: str, siddhi_MathGtLtOperation: "siddhi_MathOperation" = None):
        self.gt_eq = gt_eq
        self.lt_eq = lt_eq
        self.gt = gt
        self.lt = lt
        self.siddhi_MathGtLtOperation = siddhi_MathGtLtOperation
        
    @property
    def gt_eq(self) -> str:
        return self.__gt_eq

    @gt_eq.setter
    def gt_eq(self, gt_eq: str):
        self.__gt_eq = gt_eq

    @property
    def lt(self) -> str:
        return self.__lt

    @lt.setter
    def lt(self, lt: str):
        self.__lt = lt

    @property
    def gt(self) -> str:
        return self.__gt

    @gt.setter
    def gt(self, gt: str):
        self.__gt = gt

    @property
    def lt_eq(self) -> str:
        return self.__lt_eq

    @lt_eq.setter
    def lt_eq(self, lt_eq: str):
        self.__lt_eq = lt_eq

    @property
    def siddhi_MathGtLtOperation(self):
        return self.__siddhi_MathGtLtOperation

    @siddhi_MathGtLtOperation.setter
    def siddhi_MathGtLtOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_MathGtLtOperation__siddhi_MathGtLtOperation", None)
        self.__siddhi_MathGtLtOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathOperation668"):
                opp_val = getattr(old_value, "siddhi_MathOperation668", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathOperation668", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathOperation668"):
                opp_val = getattr(value, "siddhi_MathOperation668", None)
                setattr(value, "siddhi_MathOperation668", self)

class siddhi_MathEqualOperation(MathOperation):

    def __init__(self, eq: str, not_eq: str, siddhi_MathEqualOperation: "siddhi_MathAddsubOperation" = None):
        self.eq = eq
        self.not_eq = not_eq
        self.siddhi_MathEqualOperation = siddhi_MathEqualOperation
        
    @property
    def not_eq(self) -> str:
        return self.__not_eq

    @not_eq.setter
    def not_eq(self, not_eq: str):
        self.__not_eq = not_eq

    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

    @property
    def siddhi_MathEqualOperation(self):
        return self.__siddhi_MathEqualOperation

    @siddhi_MathEqualOperation.setter
    def siddhi_MathEqualOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_MathEqualOperation__siddhi_MathEqualOperation", None)
        self.__siddhi_MathEqualOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathAddsubOperation670"):
                opp_val = getattr(old_value, "siddhi_MathAddsubOperation670", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathAddsubOperation670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathAddsubOperation670"):
                opp_val = getattr(value, "siddhi_MathAddsubOperation670", None)
                setattr(value, "siddhi_MathAddsubOperation670", self)

class siddhi_MathAddsubOperation(MathOperation):

    def __init__(self, add: str, substract: str, siddhi_MathAddsubOperation: "siddhi_MathDivmulOperation" = None, siddhi_MathAddsubOperation670: "siddhi_MathEqualOperation" = None):
        self.add = add
        self.substract = substract
        self.siddhi_MathAddsubOperation = siddhi_MathAddsubOperation
        self.siddhi_MathAddsubOperation670 = siddhi_MathAddsubOperation670
        
    @property
    def substract(self) -> str:
        return self.__substract

    @substract.setter
    def substract(self, substract: str):
        self.__substract = substract

    @property
    def add(self) -> str:
        return self.__add

    @add.setter
    def add(self, add: str):
        self.__add = add

    @property
    def siddhi_MathAddsubOperation(self):
        return self.__siddhi_MathAddsubOperation

    @siddhi_MathAddsubOperation.setter
    def siddhi_MathAddsubOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_MathAddsubOperation__siddhi_MathAddsubOperation", None)
        self.__siddhi_MathAddsubOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathDivmulOperation"):
                opp_val = getattr(old_value, "siddhi_MathDivmulOperation", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathDivmulOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathDivmulOperation"):
                opp_val = getattr(value, "siddhi_MathDivmulOperation", None)
                setattr(value, "siddhi_MathDivmulOperation", self)

    @property
    def siddhi_MathAddsubOperation670(self):
        return self.__siddhi_MathAddsubOperation670

    @siddhi_MathAddsubOperation670.setter
    def siddhi_MathAddsubOperation670(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_MathAddsubOperation__siddhi_MathAddsubOperation670", None)
        self.__siddhi_MathAddsubOperation670 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathEqualOperation"):
                opp_val = getattr(old_value, "siddhi_MathEqualOperation", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathEqualOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathEqualOperation"):
                opp_val = getattr(value, "siddhi_MathEqualOperation", None)
                setattr(value, "siddhi_MathEqualOperation", self)

class Expression:

    pass
class siddhi_MathOperation(Expression):

    pass
class siddhi_StreamFunction:

    pass
class siddhi_Filter:

    pass
class siddhi_BasicSourceStreamHandler:

    pass
class siddhi_BasicSourceStreamHandlers:

    pass
class StandardStream:

    pass
class JoinSource:

    pass
class siddhi_MainSource(JoinSource, StandardStream):

    pass
class JoinStream:

    pass
class INNER:

    pass
class FULL:

    pass
class RIGHT:

    pass
class JOIN:

    pass
class OUTER:

    pass
class LEFT:

    pass
class PER:

    pass
class WITHIN:

    pass
class siddhi_joins(LEFT, INNER, OUTER, JOIN, FULL, RIGHT):

    pass
class siddhi_Per1(PER):

    pass
class siddhi_WithinTimeRange(WITHIN):

    pass
class siddhi_UNIDIRECTIONAL:

    def __init__(self, unidirectional: str, siddhi_UNIDIRECTIONAL: "siddhi_JoinStream" = None, siddhi_UNIDIRECTIONAL433: "siddhi_JoinStream" = None, siddhi_UNIDIRECTIONAL618: "siddhi_Keyword" = None):
        self.unidirectional = unidirectional
        self.siddhi_UNIDIRECTIONAL = siddhi_UNIDIRECTIONAL
        self.siddhi_UNIDIRECTIONAL433 = siddhi_UNIDIRECTIONAL433
        self.siddhi_UNIDIRECTIONAL618 = siddhi_UNIDIRECTIONAL618
        
    @property
    def unidirectional(self) -> str:
        return self.__unidirectional

    @unidirectional.setter
    def unidirectional(self, unidirectional: str):
        self.__unidirectional = unidirectional

    @property
    def siddhi_UNIDIRECTIONAL618(self):
        return self.__siddhi_UNIDIRECTIONAL618

    @siddhi_UNIDIRECTIONAL618.setter
    def siddhi_UNIDIRECTIONAL618(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_UNIDIRECTIONAL__siddhi_UNIDIRECTIONAL618", None)
        self.__siddhi_UNIDIRECTIONAL618 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Keyword617"):
                opp_val = getattr(old_value, "siddhi_Keyword617", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Keyword617", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Keyword617"):
                opp_val = getattr(value, "siddhi_Keyword617", None)
                setattr(value, "siddhi_Keyword617", self)

    @property
    def siddhi_UNIDIRECTIONAL(self):
        return self.__siddhi_UNIDIRECTIONAL

    @siddhi_UNIDIRECTIONAL.setter
    def siddhi_UNIDIRECTIONAL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_UNIDIRECTIONAL__siddhi_UNIDIRECTIONAL", None)
        self.__siddhi_UNIDIRECTIONAL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_JoinStream418"):
                opp_val = getattr(old_value, "siddhi_JoinStream418", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_JoinStream418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_JoinStream418"):
                opp_val = getattr(value, "siddhi_JoinStream418", None)
                setattr(value, "siddhi_JoinStream418", self)

    @property
    def siddhi_UNIDIRECTIONAL433(self):
        return self.__siddhi_UNIDIRECTIONAL433

    @siddhi_UNIDIRECTIONAL433.setter
    def siddhi_UNIDIRECTIONAL433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_UNIDIRECTIONAL__siddhi_UNIDIRECTIONAL433", None)
        self.__siddhi_UNIDIRECTIONAL433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_JoinStream432"):
                opp_val = getattr(old_value, "siddhi_JoinStream432", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_JoinStream432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_JoinStream432"):
                opp_val = getattr(value, "siddhi_JoinStream432", None)
                setattr(value, "siddhi_JoinStream432", self)

class siddhi_JoinSource:

    pass
class AbsentPatternSourceChain:

    pass
class siddhi_LeftAbsentPatternSource(AbsentPatternSourceChain):

    def __init__(self, fb1: str, siddhi_LeftAbsentPatternSource: "siddhi_LeftAbsentPatternSource" = None, siddhi_LeftAbsentPatternSource375: "siddhi_LeftAbsentPatternSource" = None, siddhi_LeftAbsentPatternSource378: "siddhi_AbsentPatternSourceChain" = None, siddhi_LeftAbsentPatternSource382: "siddhi_LeftAbsentPatternSource" = None, siddhi_LeftAbsentPatternSource380: "siddhi_LeftAbsentPatternSource" = None, siddhi_LeftAbsentPatternSource384: set["siddhi_WithinTime"] = None, siddhi_LeftAbsentPatternSource387: "siddhi_EveryAbsentPatternSource" = None, siddhi_LeftAbsentPatternSource390: "siddhi_EveryPatternSourceChain" = None, siddhi_LeftAbsentPatternSource394: "siddhi_LeftAbsentPatternSource" = None, siddhi_LeftAbsentPatternSource392: "siddhi_LeftAbsentPatternSource" = None):
        self.fb1 = fb1
        self.siddhi_LeftAbsentPatternSource = siddhi_LeftAbsentPatternSource
        self.siddhi_LeftAbsentPatternSource375 = siddhi_LeftAbsentPatternSource375
        self.siddhi_LeftAbsentPatternSource378 = siddhi_LeftAbsentPatternSource378
        self.siddhi_LeftAbsentPatternSource382 = siddhi_LeftAbsentPatternSource382
        self.siddhi_LeftAbsentPatternSource380 = siddhi_LeftAbsentPatternSource380
        self.siddhi_LeftAbsentPatternSource384 = siddhi_LeftAbsentPatternSource384 if siddhi_LeftAbsentPatternSource384 is not None else set()
        self.siddhi_LeftAbsentPatternSource387 = siddhi_LeftAbsentPatternSource387
        self.siddhi_LeftAbsentPatternSource390 = siddhi_LeftAbsentPatternSource390
        self.siddhi_LeftAbsentPatternSource394 = siddhi_LeftAbsentPatternSource394
        self.siddhi_LeftAbsentPatternSource392 = siddhi_LeftAbsentPatternSource392
        
    @property
    def fb1(self) -> str:
        return self.__fb1

    @fb1.setter
    def fb1(self, fb1: str):
        self.__fb1 = fb1

    @property
    def siddhi_LeftAbsentPatternSource(self):
        return self.__siddhi_LeftAbsentPatternSource

    @siddhi_LeftAbsentPatternSource.setter
    def siddhi_LeftAbsentPatternSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource", None)
        self.__siddhi_LeftAbsentPatternSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentPatternSource375"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentPatternSource375", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentPatternSource375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentPatternSource375"):
                opp_val = getattr(value, "siddhi_LeftAbsentPatternSource375", None)
                setattr(value, "siddhi_LeftAbsentPatternSource375", self)

    @property
    def siddhi_LeftAbsentPatternSource387(self):
        return self.__siddhi_LeftAbsentPatternSource387

    @siddhi_LeftAbsentPatternSource387.setter
    def siddhi_LeftAbsentPatternSource387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource387", None)
        self.__siddhi_LeftAbsentPatternSource387 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryAbsentPatternSource388"):
                opp_val = getattr(old_value, "siddhi_EveryAbsentPatternSource388", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryAbsentPatternSource388", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryAbsentPatternSource388"):
                opp_val = getattr(value, "siddhi_EveryAbsentPatternSource388", None)
                setattr(value, "siddhi_EveryAbsentPatternSource388", self)

    @property
    def siddhi_LeftAbsentPatternSource375(self):
        return self.__siddhi_LeftAbsentPatternSource375

    @siddhi_LeftAbsentPatternSource375.setter
    def siddhi_LeftAbsentPatternSource375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource375", None)
        self.__siddhi_LeftAbsentPatternSource375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentPatternSource"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentPatternSource", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentPatternSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentPatternSource"):
                opp_val = getattr(value, "siddhi_LeftAbsentPatternSource", None)
                setattr(value, "siddhi_LeftAbsentPatternSource", self)

    @property
    def siddhi_LeftAbsentPatternSource390(self):
        return self.__siddhi_LeftAbsentPatternSource390

    @siddhi_LeftAbsentPatternSource390.setter
    def siddhi_LeftAbsentPatternSource390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource390", None)
        self.__siddhi_LeftAbsentPatternSource390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain391"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain391", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain391", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain391"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain391", None)
                setattr(value, "siddhi_EveryPatternSourceChain391", self)

    @property
    def siddhi_LeftAbsentPatternSource394(self):
        return self.__siddhi_LeftAbsentPatternSource394

    @siddhi_LeftAbsentPatternSource394.setter
    def siddhi_LeftAbsentPatternSource394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource394", None)
        self.__siddhi_LeftAbsentPatternSource394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentPatternSource392"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentPatternSource392", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentPatternSource392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentPatternSource392"):
                opp_val = getattr(value, "siddhi_LeftAbsentPatternSource392", None)
                setattr(value, "siddhi_LeftAbsentPatternSource392", self)

    @property
    def siddhi_LeftAbsentPatternSource392(self):
        return self.__siddhi_LeftAbsentPatternSource392

    @siddhi_LeftAbsentPatternSource392.setter
    def siddhi_LeftAbsentPatternSource392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource392", None)
        self.__siddhi_LeftAbsentPatternSource392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentPatternSource394"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentPatternSource394", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentPatternSource394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentPatternSource394"):
                opp_val = getattr(value, "siddhi_LeftAbsentPatternSource394", None)
                setattr(value, "siddhi_LeftAbsentPatternSource394", self)

    @property
    def siddhi_LeftAbsentPatternSource378(self):
        return self.__siddhi_LeftAbsentPatternSource378

    @siddhi_LeftAbsentPatternSource378.setter
    def siddhi_LeftAbsentPatternSource378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource378", None)
        self.__siddhi_LeftAbsentPatternSource378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_AbsentPatternSourceChain379"):
                opp_val = getattr(old_value, "siddhi_AbsentPatternSourceChain379", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_AbsentPatternSourceChain379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_AbsentPatternSourceChain379"):
                opp_val = getattr(value, "siddhi_AbsentPatternSourceChain379", None)
                setattr(value, "siddhi_AbsentPatternSourceChain379", self)

    @property
    def siddhi_LeftAbsentPatternSource380(self):
        return self.__siddhi_LeftAbsentPatternSource380

    @siddhi_LeftAbsentPatternSource380.setter
    def siddhi_LeftAbsentPatternSource380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource380", None)
        self.__siddhi_LeftAbsentPatternSource380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentPatternSource382"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentPatternSource382", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentPatternSource382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentPatternSource382"):
                opp_val = getattr(value, "siddhi_LeftAbsentPatternSource382", None)
                setattr(value, "siddhi_LeftAbsentPatternSource382", self)

    @property
    def siddhi_LeftAbsentPatternSource384(self):
        return self.__siddhi_LeftAbsentPatternSource384

    @siddhi_LeftAbsentPatternSource384.setter
    def siddhi_LeftAbsentPatternSource384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource384", None)
        self.__siddhi_LeftAbsentPatternSource384 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "siddhi_WithinTime385"):
                    opp_val = getattr(item, "siddhi_WithinTime385", None)
                    
                    if opp_val == self:
                        setattr(item, "siddhi_WithinTime385", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "siddhi_WithinTime385"):
                    opp_val = getattr(item, "siddhi_WithinTime385", None)
                    
                    setattr(item, "siddhi_WithinTime385", self)
                    

    @property
    def siddhi_LeftAbsentPatternSource382(self):
        return self.__siddhi_LeftAbsentPatternSource382

    @siddhi_LeftAbsentPatternSource382.setter
    def siddhi_LeftAbsentPatternSource382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentPatternSource__siddhi_LeftAbsentPatternSource382", None)
        self.__siddhi_LeftAbsentPatternSource382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentPatternSource380"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentPatternSource380", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentPatternSource380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentPatternSource380"):
                opp_val = getattr(value, "siddhi_LeftAbsentPatternSource380", None)
                setattr(value, "siddhi_LeftAbsentPatternSource380", self)

class siddhi_RightAbsentPatternSource(AbsentPatternSourceChain):

    def __init__(self, fb2: str, siddhi_RightAbsentPatternSource: "siddhi_RightAbsentPatternSource" = None, siddhi_RightAbsentPatternSource395: "siddhi_RightAbsentPatternSource" = None, siddhi_RightAbsentPatternSource399: "siddhi_RightAbsentPatternSource" = None, siddhi_RightAbsentPatternSource397: "siddhi_RightAbsentPatternSource" = None, siddhi_RightAbsentPatternSource402: "siddhi_RightAbsentPatternSource" = None, siddhi_RightAbsentPatternSource400: "siddhi_RightAbsentPatternSource" = None, siddhi_RightAbsentPatternSource404: set["siddhi_WithinTime"] = None, siddhi_RightAbsentPatternSource407: "siddhi_EveryPatternSourceChain" = None, siddhi_RightAbsentPatternSource410: "siddhi_EveryAbsentPatternSource" = None, siddhi_RightAbsentPatternSource651: "siddhi_RightAbsentPatternSource1" = None):
        self.fb2 = fb2
        self.siddhi_RightAbsentPatternSource = siddhi_RightAbsentPatternSource
        self.siddhi_RightAbsentPatternSource395 = siddhi_RightAbsentPatternSource395
        self.siddhi_RightAbsentPatternSource399 = siddhi_RightAbsentPatternSource399
        self.siddhi_RightAbsentPatternSource397 = siddhi_RightAbsentPatternSource397
        self.siddhi_RightAbsentPatternSource402 = siddhi_RightAbsentPatternSource402
        self.siddhi_RightAbsentPatternSource400 = siddhi_RightAbsentPatternSource400
        self.siddhi_RightAbsentPatternSource404 = siddhi_RightAbsentPatternSource404 if siddhi_RightAbsentPatternSource404 is not None else set()
        self.siddhi_RightAbsentPatternSource407 = siddhi_RightAbsentPatternSource407
        self.siddhi_RightAbsentPatternSource410 = siddhi_RightAbsentPatternSource410
        self.siddhi_RightAbsentPatternSource651 = siddhi_RightAbsentPatternSource651
        
    @property
    def fb2(self) -> str:
        return self.__fb2

    @fb2.setter
    def fb2(self, fb2: str):
        self.__fb2 = fb2

    @property
    def siddhi_RightAbsentPatternSource399(self):
        return self.__siddhi_RightAbsentPatternSource399

    @siddhi_RightAbsentPatternSource399.setter
    def siddhi_RightAbsentPatternSource399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource399", None)
        self.__siddhi_RightAbsentPatternSource399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource397"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource397", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource397"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource397", None)
                setattr(value, "siddhi_RightAbsentPatternSource397", self)

    @property
    def siddhi_RightAbsentPatternSource397(self):
        return self.__siddhi_RightAbsentPatternSource397

    @siddhi_RightAbsentPatternSource397.setter
    def siddhi_RightAbsentPatternSource397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource397", None)
        self.__siddhi_RightAbsentPatternSource397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource399"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource399", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource399"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource399", None)
                setattr(value, "siddhi_RightAbsentPatternSource399", self)

    @property
    def siddhi_RightAbsentPatternSource(self):
        return self.__siddhi_RightAbsentPatternSource

    @siddhi_RightAbsentPatternSource.setter
    def siddhi_RightAbsentPatternSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource", None)
        self.__siddhi_RightAbsentPatternSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource395"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource395", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource395"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource395", None)
                setattr(value, "siddhi_RightAbsentPatternSource395", self)

    @property
    def siddhi_RightAbsentPatternSource407(self):
        return self.__siddhi_RightAbsentPatternSource407

    @siddhi_RightAbsentPatternSource407.setter
    def siddhi_RightAbsentPatternSource407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource407", None)
        self.__siddhi_RightAbsentPatternSource407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain408"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain408", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain408"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain408", None)
                setattr(value, "siddhi_EveryPatternSourceChain408", self)

    @property
    def siddhi_RightAbsentPatternSource400(self):
        return self.__siddhi_RightAbsentPatternSource400

    @siddhi_RightAbsentPatternSource400.setter
    def siddhi_RightAbsentPatternSource400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource400", None)
        self.__siddhi_RightAbsentPatternSource400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource402"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource402", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource402"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource402", None)
                setattr(value, "siddhi_RightAbsentPatternSource402", self)

    @property
    def siddhi_RightAbsentPatternSource404(self):
        return self.__siddhi_RightAbsentPatternSource404

    @siddhi_RightAbsentPatternSource404.setter
    def siddhi_RightAbsentPatternSource404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource404", None)
        self.__siddhi_RightAbsentPatternSource404 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "siddhi_WithinTime405"):
                    opp_val = getattr(item, "siddhi_WithinTime405", None)
                    
                    if opp_val == self:
                        setattr(item, "siddhi_WithinTime405", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "siddhi_WithinTime405"):
                    opp_val = getattr(item, "siddhi_WithinTime405", None)
                    
                    setattr(item, "siddhi_WithinTime405", self)
                    

    @property
    def siddhi_RightAbsentPatternSource651(self):
        return self.__siddhi_RightAbsentPatternSource651

    @siddhi_RightAbsentPatternSource651.setter
    def siddhi_RightAbsentPatternSource651(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource651", None)
        self.__siddhi_RightAbsentPatternSource651 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource1"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource1", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource1"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource1", None)
                setattr(value, "siddhi_RightAbsentPatternSource1", self)

    @property
    def siddhi_RightAbsentPatternSource402(self):
        return self.__siddhi_RightAbsentPatternSource402

    @siddhi_RightAbsentPatternSource402.setter
    def siddhi_RightAbsentPatternSource402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource402", None)
        self.__siddhi_RightAbsentPatternSource402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource400"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource400", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource400"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource400", None)
                setattr(value, "siddhi_RightAbsentPatternSource400", self)

    @property
    def siddhi_RightAbsentPatternSource395(self):
        return self.__siddhi_RightAbsentPatternSource395

    @siddhi_RightAbsentPatternSource395.setter
    def siddhi_RightAbsentPatternSource395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource395", None)
        self.__siddhi_RightAbsentPatternSource395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource", None)
                setattr(value, "siddhi_RightAbsentPatternSource", self)

    @property
    def siddhi_RightAbsentPatternSource410(self):
        return self.__siddhi_RightAbsentPatternSource410

    @siddhi_RightAbsentPatternSource410.setter
    def siddhi_RightAbsentPatternSource410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentPatternSource__siddhi_RightAbsentPatternSource410", None)
        self.__siddhi_RightAbsentPatternSource410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryAbsentPatternSource411"):
                opp_val = getattr(old_value, "siddhi_EveryAbsentPatternSource411", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryAbsentPatternSource411", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryAbsentPatternSource411"):
                opp_val = getattr(value, "siddhi_EveryAbsentPatternSource411", None)
                setattr(value, "siddhi_EveryAbsentPatternSource411", self)

class siddhi_EveryAbsentPatternSource(AbsentPatternSourceChain):

    pass
class siddhi_BasicSource:

    pass
class siddhi_NOT(BasicAbsentPatternSource, LogicalAbsentStatefulSource):

    def __init__(self, not1: str, siddhi_NOT: "siddhi_LogicalAbsentStatefulSource" = None, siddhi_NOT630: "siddhi_Keyword" = None, siddhi_NOT635: "siddhi_BasicSource" = None, siddhi_NOT638: "siddhi_ForTime" = None, siddhi_NOT672: "siddhi_NotOperation" = None):
        self.not1 = not1
        self.siddhi_NOT = siddhi_NOT
        self.siddhi_NOT630 = siddhi_NOT630
        self.siddhi_NOT635 = siddhi_NOT635
        self.siddhi_NOT638 = siddhi_NOT638
        self.siddhi_NOT672 = siddhi_NOT672
        
    @property
    def not1(self) -> str:
        return self.__not1

    @not1.setter
    def not1(self, not1: str):
        self.__not1 = not1

    @property
    def siddhi_NOT638(self):
        return self.__siddhi_NOT638

    @siddhi_NOT638.setter
    def siddhi_NOT638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_NOT__siddhi_NOT638", None)
        self.__siddhi_NOT638 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_ForTime639"):
                opp_val = getattr(old_value, "siddhi_ForTime639", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_ForTime639", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_ForTime639"):
                opp_val = getattr(value, "siddhi_ForTime639", None)
                setattr(value, "siddhi_ForTime639", self)

    @property
    def siddhi_NOT630(self):
        return self.__siddhi_NOT630

    @siddhi_NOT630.setter
    def siddhi_NOT630(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_NOT__siddhi_NOT630", None)
        self.__siddhi_NOT630 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Keyword629"):
                opp_val = getattr(old_value, "siddhi_Keyword629", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Keyword629", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Keyword629"):
                opp_val = getattr(value, "siddhi_Keyword629", None)
                setattr(value, "siddhi_Keyword629", self)

    @property
    def siddhi_NOT672(self):
        return self.__siddhi_NOT672

    @siddhi_NOT672.setter
    def siddhi_NOT672(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_NOT__siddhi_NOT672", None)
        self.__siddhi_NOT672 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_NotOperation"):
                opp_val = getattr(old_value, "siddhi_NotOperation", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_NotOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_NotOperation"):
                opp_val = getattr(value, "siddhi_NotOperation", None)
                setattr(value, "siddhi_NotOperation", self)

    @property
    def siddhi_NOT(self):
        return self.__siddhi_NOT

    @siddhi_NOT.setter
    def siddhi_NOT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_NOT__siddhi_NOT", None)
        self.__siddhi_NOT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LogicalAbsentStatefulSource351"):
                opp_val = getattr(old_value, "siddhi_LogicalAbsentStatefulSource351", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LogicalAbsentStatefulSource351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LogicalAbsentStatefulSource351"):
                opp_val = getattr(value, "siddhi_LogicalAbsentStatefulSource351", None)
                setattr(value, "siddhi_LogicalAbsentStatefulSource351", self)

    @property
    def siddhi_NOT635(self):
        return self.__siddhi_NOT635

    @siddhi_NOT635.setter
    def siddhi_NOT635(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_NOT__siddhi_NOT635", None)
        self.__siddhi_NOT635 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_BasicSource636"):
                opp_val = getattr(old_value, "siddhi_BasicSource636", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_BasicSource636", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_BasicSource636"):
                opp_val = getattr(value, "siddhi_BasicSource636", None)
                setattr(value, "siddhi_BasicSource636", self)

class siddhi_Collect:

    def __init__(self, start: str, end: str, siddhi_Collect: "siddhi_StandardStatefulSource" = None):
        self.start = start
        self.end = end
        self.siddhi_Collect = siddhi_Collect
        
    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def siddhi_Collect(self):
        return self.__siddhi_Collect

    @siddhi_Collect.setter
    def siddhi_Collect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Collect__siddhi_Collect", None)
        self.__siddhi_Collect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_StandardStatefulSource535"):
                opp_val = getattr(old_value, "siddhi_StandardStatefulSource535", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_StandardStatefulSource535", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_StandardStatefulSource535"):
                opp_val = getattr(value, "siddhi_StandardStatefulSource535", None)
                setattr(value, "siddhi_StandardStatefulSource535", self)

class siddhi_AND:

    def __init__(self, and: str, siddhi_AND: "siddhi_LogicalStatefulSource" = None, siddhi_AND349: "siddhi_LogicalAbsentStatefulSource" = None, siddhi_AND624: "siddhi_Keyword" = None, siddhi_AND656: "siddhi_MathLogicalOperation" = None):
        self.and = and
        self.siddhi_AND = siddhi_AND
        self.siddhi_AND349 = siddhi_AND349
        self.siddhi_AND624 = siddhi_AND624
        self.siddhi_AND656 = siddhi_AND656
        
    @property
    def and(self) -> str:
        return self.__and

    @and.setter
    def and(self, and: str):
        self.__and = and

    @property
    def siddhi_AND624(self):
        return self.__siddhi_AND624

    @siddhi_AND624.setter
    def siddhi_AND624(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AND__siddhi_AND624", None)
        self.__siddhi_AND624 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Keyword623"):
                opp_val = getattr(old_value, "siddhi_Keyword623", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Keyword623", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Keyword623"):
                opp_val = getattr(value, "siddhi_Keyword623", None)
                setattr(value, "siddhi_Keyword623", self)

    @property
    def siddhi_AND656(self):
        return self.__siddhi_AND656

    @siddhi_AND656.setter
    def siddhi_AND656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AND__siddhi_AND656", None)
        self.__siddhi_AND656 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathLogicalOperation"):
                opp_val = getattr(old_value, "siddhi_MathLogicalOperation", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathLogicalOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathLogicalOperation"):
                opp_val = getattr(value, "siddhi_MathLogicalOperation", None)
                setattr(value, "siddhi_MathLogicalOperation", self)

    @property
    def siddhi_AND349(self):
        return self.__siddhi_AND349

    @siddhi_AND349.setter
    def siddhi_AND349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AND__siddhi_AND349", None)
        self.__siddhi_AND349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LogicalAbsentStatefulSource348"):
                opp_val = getattr(old_value, "siddhi_LogicalAbsentStatefulSource348", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LogicalAbsentStatefulSource348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LogicalAbsentStatefulSource348"):
                opp_val = getattr(value, "siddhi_LogicalAbsentStatefulSource348", None)
                setattr(value, "siddhi_LogicalAbsentStatefulSource348", self)

    @property
    def siddhi_AND(self):
        return self.__siddhi_AND

    @siddhi_AND.setter
    def siddhi_AND(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AND__siddhi_AND", None)
        self.__siddhi_AND = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LogicalStatefulSource337"):
                opp_val = getattr(old_value, "siddhi_LogicalStatefulSource337", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LogicalStatefulSource337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LogicalStatefulSource337"):
                opp_val = getattr(value, "siddhi_LogicalStatefulSource337", None)
                setattr(value, "siddhi_LogicalStatefulSource337", self)

class siddhi_PatternCollectionStatefulSource:

    pass
class siddhi_PatternSource:

    pass
class siddhi_PatternSourceChain:

    def __init__(self, op: str, siddhi_PatternSourceChain: "siddhi_EveryPatternSourceChain" = None, siddhi_PatternSourceChain313: "siddhi_PatternSourceChain" = None, siddhi_PatternSourceChain311: "siddhi_PatternSourceChain" = None, siddhi_PatternSourceChain316: "siddhi_PatternSourceChain" = None, siddhi_PatternSourceChain314: "siddhi_PatternSourceChain" = None, siddhi_PatternSourceChain319: "siddhi_PatternSourceChain" = None, siddhi_PatternSourceChain317: "siddhi_PatternSourceChain" = None, siddhi_PatternSourceChain321: "siddhi_WithinTime" = None, siddhi_PatternSourceChain324: "siddhi_PatternSource" = None):
        self.op = op
        self.siddhi_PatternSourceChain = siddhi_PatternSourceChain
        self.siddhi_PatternSourceChain313 = siddhi_PatternSourceChain313
        self.siddhi_PatternSourceChain311 = siddhi_PatternSourceChain311
        self.siddhi_PatternSourceChain316 = siddhi_PatternSourceChain316
        self.siddhi_PatternSourceChain314 = siddhi_PatternSourceChain314
        self.siddhi_PatternSourceChain319 = siddhi_PatternSourceChain319
        self.siddhi_PatternSourceChain317 = siddhi_PatternSourceChain317
        self.siddhi_PatternSourceChain321 = siddhi_PatternSourceChain321
        self.siddhi_PatternSourceChain324 = siddhi_PatternSourceChain324
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def siddhi_PatternSourceChain317(self):
        return self.__siddhi_PatternSourceChain317

    @siddhi_PatternSourceChain317.setter
    def siddhi_PatternSourceChain317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain317", None)
        self.__siddhi_PatternSourceChain317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSourceChain319"):
                opp_val = getattr(old_value, "siddhi_PatternSourceChain319", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSourceChain319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSourceChain319"):
                opp_val = getattr(value, "siddhi_PatternSourceChain319", None)
                setattr(value, "siddhi_PatternSourceChain319", self)

    @property
    def siddhi_PatternSourceChain(self):
        return self.__siddhi_PatternSourceChain

    @siddhi_PatternSourceChain.setter
    def siddhi_PatternSourceChain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain", None)
        self.__siddhi_PatternSourceChain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain307"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain307", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain307"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain307", None)
                setattr(value, "siddhi_EveryPatternSourceChain307", self)

    @property
    def siddhi_PatternSourceChain319(self):
        return self.__siddhi_PatternSourceChain319

    @siddhi_PatternSourceChain319.setter
    def siddhi_PatternSourceChain319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain319", None)
        self.__siddhi_PatternSourceChain319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSourceChain317"):
                opp_val = getattr(old_value, "siddhi_PatternSourceChain317", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSourceChain317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSourceChain317"):
                opp_val = getattr(value, "siddhi_PatternSourceChain317", None)
                setattr(value, "siddhi_PatternSourceChain317", self)

    @property
    def siddhi_PatternSourceChain314(self):
        return self.__siddhi_PatternSourceChain314

    @siddhi_PatternSourceChain314.setter
    def siddhi_PatternSourceChain314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain314", None)
        self.__siddhi_PatternSourceChain314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSourceChain316"):
                opp_val = getattr(old_value, "siddhi_PatternSourceChain316", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSourceChain316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSourceChain316"):
                opp_val = getattr(value, "siddhi_PatternSourceChain316", None)
                setattr(value, "siddhi_PatternSourceChain316", self)

    @property
    def siddhi_PatternSourceChain324(self):
        return self.__siddhi_PatternSourceChain324

    @siddhi_PatternSourceChain324.setter
    def siddhi_PatternSourceChain324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain324", None)
        self.__siddhi_PatternSourceChain324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSource"):
                opp_val = getattr(old_value, "siddhi_PatternSource", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSource"):
                opp_val = getattr(value, "siddhi_PatternSource", None)
                setattr(value, "siddhi_PatternSource", self)

    @property
    def siddhi_PatternSourceChain313(self):
        return self.__siddhi_PatternSourceChain313

    @siddhi_PatternSourceChain313.setter
    def siddhi_PatternSourceChain313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain313", None)
        self.__siddhi_PatternSourceChain313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSourceChain311"):
                opp_val = getattr(old_value, "siddhi_PatternSourceChain311", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSourceChain311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSourceChain311"):
                opp_val = getattr(value, "siddhi_PatternSourceChain311", None)
                setattr(value, "siddhi_PatternSourceChain311", self)

    @property
    def siddhi_PatternSourceChain311(self):
        return self.__siddhi_PatternSourceChain311

    @siddhi_PatternSourceChain311.setter
    def siddhi_PatternSourceChain311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain311", None)
        self.__siddhi_PatternSourceChain311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSourceChain313"):
                opp_val = getattr(old_value, "siddhi_PatternSourceChain313", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSourceChain313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSourceChain313"):
                opp_val = getattr(value, "siddhi_PatternSourceChain313", None)
                setattr(value, "siddhi_PatternSourceChain313", self)

    @property
    def siddhi_PatternSourceChain321(self):
        return self.__siddhi_PatternSourceChain321

    @siddhi_PatternSourceChain321.setter
    def siddhi_PatternSourceChain321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain321", None)
        self.__siddhi_PatternSourceChain321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_WithinTime322"):
                opp_val = getattr(old_value, "siddhi_WithinTime322", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_WithinTime322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_WithinTime322"):
                opp_val = getattr(value, "siddhi_WithinTime322", None)
                setattr(value, "siddhi_WithinTime322", self)

    @property
    def siddhi_PatternSourceChain316(self):
        return self.__siddhi_PatternSourceChain316

    @siddhi_PatternSourceChain316.setter
    def siddhi_PatternSourceChain316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_PatternSourceChain__siddhi_PatternSourceChain316", None)
        self.__siddhi_PatternSourceChain316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSourceChain314"):
                opp_val = getattr(old_value, "siddhi_PatternSourceChain314", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSourceChain314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSourceChain314"):
                opp_val = getattr(value, "siddhi_PatternSourceChain314", None)
                setattr(value, "siddhi_PatternSourceChain314", self)

class PatternStream:

    pass
class siddhi_AbsentPatternSourceChain(PatternStream):

    pass
class siddhi_EveryPatternSourceChain(PatternStream):

    def __init__(self, op: str, siddhi_EveryPatternSourceChain: "siddhi_EveryPatternSourceChain" = None, siddhi_EveryPatternSourceChain295: "siddhi_EveryPatternSourceChain" = None, siddhi_EveryPatternSourceChain299: "siddhi_EveryPatternSourceChain" = None, siddhi_EveryPatternSourceChain297: "siddhi_EveryPatternSourceChain" = None, siddhi_EveryPatternSourceChain302: "siddhi_EveryPatternSourceChain" = None, siddhi_EveryPatternSourceChain300: "siddhi_EveryPatternSourceChain" = None, siddhi_EveryPatternSourceChain304: "siddhi_WithinTime" = None, siddhi_EveryPatternSourceChain307: "siddhi_PatternSourceChain" = None, siddhi_EveryPatternSourceChain309: "siddhi_EVERY" = None, siddhi_EveryPatternSourceChain391: "siddhi_LeftAbsentPatternSource" = None, siddhi_EveryPatternSourceChain408: "siddhi_RightAbsentPatternSource" = None):
        self.op = op
        self.siddhi_EveryPatternSourceChain = siddhi_EveryPatternSourceChain
        self.siddhi_EveryPatternSourceChain295 = siddhi_EveryPatternSourceChain295
        self.siddhi_EveryPatternSourceChain299 = siddhi_EveryPatternSourceChain299
        self.siddhi_EveryPatternSourceChain297 = siddhi_EveryPatternSourceChain297
        self.siddhi_EveryPatternSourceChain302 = siddhi_EveryPatternSourceChain302
        self.siddhi_EveryPatternSourceChain300 = siddhi_EveryPatternSourceChain300
        self.siddhi_EveryPatternSourceChain304 = siddhi_EveryPatternSourceChain304
        self.siddhi_EveryPatternSourceChain307 = siddhi_EveryPatternSourceChain307
        self.siddhi_EveryPatternSourceChain309 = siddhi_EveryPatternSourceChain309
        self.siddhi_EveryPatternSourceChain391 = siddhi_EveryPatternSourceChain391
        self.siddhi_EveryPatternSourceChain408 = siddhi_EveryPatternSourceChain408
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def siddhi_EveryPatternSourceChain299(self):
        return self.__siddhi_EveryPatternSourceChain299

    @siddhi_EveryPatternSourceChain299.setter
    def siddhi_EveryPatternSourceChain299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain299", None)
        self.__siddhi_EveryPatternSourceChain299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain297"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain297", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain297"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain297", None)
                setattr(value, "siddhi_EveryPatternSourceChain297", self)

    @property
    def siddhi_EveryPatternSourceChain295(self):
        return self.__siddhi_EveryPatternSourceChain295

    @siddhi_EveryPatternSourceChain295.setter
    def siddhi_EveryPatternSourceChain295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain295", None)
        self.__siddhi_EveryPatternSourceChain295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain", None)
                setattr(value, "siddhi_EveryPatternSourceChain", self)

    @property
    def siddhi_EveryPatternSourceChain309(self):
        return self.__siddhi_EveryPatternSourceChain309

    @siddhi_EveryPatternSourceChain309.setter
    def siddhi_EveryPatternSourceChain309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain309", None)
        self.__siddhi_EveryPatternSourceChain309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EVERY310"):
                opp_val = getattr(old_value, "siddhi_EVERY310", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EVERY310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EVERY310"):
                opp_val = getattr(value, "siddhi_EVERY310", None)
                setattr(value, "siddhi_EVERY310", self)

    @property
    def siddhi_EveryPatternSourceChain302(self):
        return self.__siddhi_EveryPatternSourceChain302

    @siddhi_EveryPatternSourceChain302.setter
    def siddhi_EveryPatternSourceChain302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain302", None)
        self.__siddhi_EveryPatternSourceChain302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain300"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain300", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain300"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain300", None)
                setattr(value, "siddhi_EveryPatternSourceChain300", self)

    @property
    def siddhi_EveryPatternSourceChain304(self):
        return self.__siddhi_EveryPatternSourceChain304

    @siddhi_EveryPatternSourceChain304.setter
    def siddhi_EveryPatternSourceChain304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain304", None)
        self.__siddhi_EveryPatternSourceChain304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_WithinTime305"):
                opp_val = getattr(old_value, "siddhi_WithinTime305", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_WithinTime305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_WithinTime305"):
                opp_val = getattr(value, "siddhi_WithinTime305", None)
                setattr(value, "siddhi_WithinTime305", self)

    @property
    def siddhi_EveryPatternSourceChain(self):
        return self.__siddhi_EveryPatternSourceChain

    @siddhi_EveryPatternSourceChain.setter
    def siddhi_EveryPatternSourceChain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain", None)
        self.__siddhi_EveryPatternSourceChain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain295"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain295", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain295"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain295", None)
                setattr(value, "siddhi_EveryPatternSourceChain295", self)

    @property
    def siddhi_EveryPatternSourceChain297(self):
        return self.__siddhi_EveryPatternSourceChain297

    @siddhi_EveryPatternSourceChain297.setter
    def siddhi_EveryPatternSourceChain297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain297", None)
        self.__siddhi_EveryPatternSourceChain297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain299"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain299", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain299"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain299", None)
                setattr(value, "siddhi_EveryPatternSourceChain299", self)

    @property
    def siddhi_EveryPatternSourceChain307(self):
        return self.__siddhi_EveryPatternSourceChain307

    @siddhi_EveryPatternSourceChain307.setter
    def siddhi_EveryPatternSourceChain307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain307", None)
        self.__siddhi_EveryPatternSourceChain307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSourceChain"):
                opp_val = getattr(old_value, "siddhi_PatternSourceChain", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSourceChain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSourceChain"):
                opp_val = getattr(value, "siddhi_PatternSourceChain", None)
                setattr(value, "siddhi_PatternSourceChain", self)

    @property
    def siddhi_EveryPatternSourceChain300(self):
        return self.__siddhi_EveryPatternSourceChain300

    @siddhi_EveryPatternSourceChain300.setter
    def siddhi_EveryPatternSourceChain300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain300", None)
        self.__siddhi_EveryPatternSourceChain300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain302"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain302", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain302"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain302", None)
                setattr(value, "siddhi_EveryPatternSourceChain302", self)

    @property
    def siddhi_EveryPatternSourceChain391(self):
        return self.__siddhi_EveryPatternSourceChain391

    @siddhi_EveryPatternSourceChain391.setter
    def siddhi_EveryPatternSourceChain391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain391", None)
        self.__siddhi_EveryPatternSourceChain391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentPatternSource390"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentPatternSource390", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentPatternSource390", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentPatternSource390"):
                opp_val = getattr(value, "siddhi_LeftAbsentPatternSource390", None)
                setattr(value, "siddhi_LeftAbsentPatternSource390", self)

    @property
    def siddhi_EveryPatternSourceChain408(self):
        return self.__siddhi_EveryPatternSourceChain408

    @siddhi_EveryPatternSourceChain408.setter
    def siddhi_EveryPatternSourceChain408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EveryPatternSourceChain__siddhi_EveryPatternSourceChain408", None)
        self.__siddhi_EveryPatternSourceChain408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentPatternSource407"):
                opp_val = getattr(old_value, "siddhi_RightAbsentPatternSource407", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentPatternSource407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentPatternSource407"):
                opp_val = getattr(value, "siddhi_RightAbsentPatternSource407", None)
                setattr(value, "siddhi_RightAbsentPatternSource407", self)

class SequenceSource:

    pass
class siddhi_LogicalStatefulSource(SequenceSource):

    pass
class siddhi_LogicalAbsentStatefulSource(SequenceSource):

    pass
class siddhi_SequenceCollectionStatefulSource(SequenceSource):

    pass
class SequenceSourceChain:

    pass
class siddhi_EObject:

    pass
class siddhi_LeftAbsentSequenceSource:

    def __init__(self, comm: str, op: str, cp: str, comma: str, siddhi_LeftAbsentSequenceSource: "siddhi_AbsentSequenceSourceChain" = None, siddhi_LeftAbsentSequenceSource238: "siddhi_LeftAbsentSequenceSource" = None, siddhi_LeftAbsentSequenceSource236: "siddhi_LeftAbsentSequenceSource" = None, siddhi_LeftAbsentSequenceSource240: "siddhi_EObject" = None, siddhi_LeftAbsentSequenceSource243: "siddhi_LeftAbsentSequenceSource" = None, siddhi_LeftAbsentSequenceSource241: "siddhi_LeftAbsentSequenceSource" = None, siddhi_LeftAbsentSequenceSource245: "siddhi_WithinTime" = None, siddhi_LeftAbsentSequenceSource248: "siddhi_BasicAbsentPatternSource" = None, siddhi_LeftAbsentSequenceSource251: "siddhi_SequenceSourceChain" = None):
        self.comm = comm
        self.op = op
        self.cp = cp
        self.comma = comma
        self.siddhi_LeftAbsentSequenceSource = siddhi_LeftAbsentSequenceSource
        self.siddhi_LeftAbsentSequenceSource238 = siddhi_LeftAbsentSequenceSource238
        self.siddhi_LeftAbsentSequenceSource236 = siddhi_LeftAbsentSequenceSource236
        self.siddhi_LeftAbsentSequenceSource240 = siddhi_LeftAbsentSequenceSource240
        self.siddhi_LeftAbsentSequenceSource243 = siddhi_LeftAbsentSequenceSource243
        self.siddhi_LeftAbsentSequenceSource241 = siddhi_LeftAbsentSequenceSource241
        self.siddhi_LeftAbsentSequenceSource245 = siddhi_LeftAbsentSequenceSource245
        self.siddhi_LeftAbsentSequenceSource248 = siddhi_LeftAbsentSequenceSource248
        self.siddhi_LeftAbsentSequenceSource251 = siddhi_LeftAbsentSequenceSource251
        
    @property
    def comma(self) -> str:
        return self.__comma

    @comma.setter
    def comma(self, comma: str):
        self.__comma = comma

    @property
    def comm(self) -> str:
        return self.__comm

    @comm.setter
    def comm(self, comm: str):
        self.__comm = comm

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def cp(self) -> str:
        return self.__cp

    @cp.setter
    def cp(self, cp: str):
        self.__cp = cp

    @property
    def siddhi_LeftAbsentSequenceSource236(self):
        return self.__siddhi_LeftAbsentSequenceSource236

    @siddhi_LeftAbsentSequenceSource236.setter
    def siddhi_LeftAbsentSequenceSource236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource236", None)
        self.__siddhi_LeftAbsentSequenceSource236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentSequenceSource238"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentSequenceSource238", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentSequenceSource238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentSequenceSource238"):
                opp_val = getattr(value, "siddhi_LeftAbsentSequenceSource238", None)
                setattr(value, "siddhi_LeftAbsentSequenceSource238", self)

    @property
    def siddhi_LeftAbsentSequenceSource238(self):
        return self.__siddhi_LeftAbsentSequenceSource238

    @siddhi_LeftAbsentSequenceSource238.setter
    def siddhi_LeftAbsentSequenceSource238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource238", None)
        self.__siddhi_LeftAbsentSequenceSource238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentSequenceSource236"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentSequenceSource236", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentSequenceSource236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentSequenceSource236"):
                opp_val = getattr(value, "siddhi_LeftAbsentSequenceSource236", None)
                setattr(value, "siddhi_LeftAbsentSequenceSource236", self)

    @property
    def siddhi_LeftAbsentSequenceSource251(self):
        return self.__siddhi_LeftAbsentSequenceSource251

    @siddhi_LeftAbsentSequenceSource251.setter
    def siddhi_LeftAbsentSequenceSource251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource251", None)
        self.__siddhi_LeftAbsentSequenceSource251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SequenceSourceChain252"):
                opp_val = getattr(old_value, "siddhi_SequenceSourceChain252", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SequenceSourceChain252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SequenceSourceChain252"):
                opp_val = getattr(value, "siddhi_SequenceSourceChain252", None)
                setattr(value, "siddhi_SequenceSourceChain252", self)

    @property
    def siddhi_LeftAbsentSequenceSource241(self):
        return self.__siddhi_LeftAbsentSequenceSource241

    @siddhi_LeftAbsentSequenceSource241.setter
    def siddhi_LeftAbsentSequenceSource241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource241", None)
        self.__siddhi_LeftAbsentSequenceSource241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentSequenceSource243"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentSequenceSource243", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentSequenceSource243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentSequenceSource243"):
                opp_val = getattr(value, "siddhi_LeftAbsentSequenceSource243", None)
                setattr(value, "siddhi_LeftAbsentSequenceSource243", self)

    @property
    def siddhi_LeftAbsentSequenceSource245(self):
        return self.__siddhi_LeftAbsentSequenceSource245

    @siddhi_LeftAbsentSequenceSource245.setter
    def siddhi_LeftAbsentSequenceSource245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource245", None)
        self.__siddhi_LeftAbsentSequenceSource245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_WithinTime246"):
                opp_val = getattr(old_value, "siddhi_WithinTime246", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_WithinTime246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_WithinTime246"):
                opp_val = getattr(value, "siddhi_WithinTime246", None)
                setattr(value, "siddhi_WithinTime246", self)

    @property
    def siddhi_LeftAbsentSequenceSource(self):
        return self.__siddhi_LeftAbsentSequenceSource

    @siddhi_LeftAbsentSequenceSource.setter
    def siddhi_LeftAbsentSequenceSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource", None)
        self.__siddhi_LeftAbsentSequenceSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_AbsentSequenceSourceChain233"):
                opp_val = getattr(old_value, "siddhi_AbsentSequenceSourceChain233", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_AbsentSequenceSourceChain233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_AbsentSequenceSourceChain233"):
                opp_val = getattr(value, "siddhi_AbsentSequenceSourceChain233", None)
                setattr(value, "siddhi_AbsentSequenceSourceChain233", self)

    @property
    def siddhi_LeftAbsentSequenceSource240(self):
        return self.__siddhi_LeftAbsentSequenceSource240

    @siddhi_LeftAbsentSequenceSource240.setter
    def siddhi_LeftAbsentSequenceSource240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource240", None)
        self.__siddhi_LeftAbsentSequenceSource240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EObject"):
                opp_val = getattr(old_value, "siddhi_EObject", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EObject"):
                opp_val = getattr(value, "siddhi_EObject", None)
                setattr(value, "siddhi_EObject", self)

    @property
    def siddhi_LeftAbsentSequenceSource248(self):
        return self.__siddhi_LeftAbsentSequenceSource248

    @siddhi_LeftAbsentSequenceSource248.setter
    def siddhi_LeftAbsentSequenceSource248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource248", None)
        self.__siddhi_LeftAbsentSequenceSource248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_BasicAbsentPatternSource249"):
                opp_val = getattr(old_value, "siddhi_BasicAbsentPatternSource249", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_BasicAbsentPatternSource249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_BasicAbsentPatternSource249"):
                opp_val = getattr(value, "siddhi_BasicAbsentPatternSource249", None)
                setattr(value, "siddhi_BasicAbsentPatternSource249", self)

    @property
    def siddhi_LeftAbsentSequenceSource243(self):
        return self.__siddhi_LeftAbsentSequenceSource243

    @siddhi_LeftAbsentSequenceSource243.setter
    def siddhi_LeftAbsentSequenceSource243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LeftAbsentSequenceSource__siddhi_LeftAbsentSequenceSource243", None)
        self.__siddhi_LeftAbsentSequenceSource243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentSequenceSource241"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentSequenceSource241", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentSequenceSource241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentSequenceSource241"):
                opp_val = getattr(value, "siddhi_LeftAbsentSequenceSource241", None)
                setattr(value, "siddhi_LeftAbsentSequenceSource241", self)

class siddhi_BasicAbsentPatternSource:

    pass
class siddhi_AbsentSequenceSourceChain:

    pass
class siddhi_SequenceSourceChain:

    def __init__(self, op: str, siddhi_SequenceSourceChain: "siddhi_EverySequenceSourceChain" = None, siddhi_SequenceSourceChain223: "siddhi_EveryAbsentSequenceSourceChain" = None, siddhi_SequenceSourceChain252: "siddhi_LeftAbsentSequenceSource" = None, siddhi_SequenceSourceChain267: "siddhi_RightAbsentSequenceSource" = None, siddhi_SequenceSourceChain273: "siddhi_SequenceSourceChain" = None, siddhi_SequenceSourceChain271: "siddhi_SequenceSourceChain" = None, siddhi_SequenceSourceChain276: "siddhi_SequenceSourceChain" = None, siddhi_SequenceSourceChain274: "siddhi_SequenceSourceChain" = None, siddhi_SequenceSourceChain278: set["siddhi_WithinTime"] = None, siddhi_SequenceSourceChain649: "siddhi_RightAbsentSequenceSource1" = None):
        self.op = op
        self.siddhi_SequenceSourceChain = siddhi_SequenceSourceChain
        self.siddhi_SequenceSourceChain223 = siddhi_SequenceSourceChain223
        self.siddhi_SequenceSourceChain252 = siddhi_SequenceSourceChain252
        self.siddhi_SequenceSourceChain267 = siddhi_SequenceSourceChain267
        self.siddhi_SequenceSourceChain273 = siddhi_SequenceSourceChain273
        self.siddhi_SequenceSourceChain271 = siddhi_SequenceSourceChain271
        self.siddhi_SequenceSourceChain276 = siddhi_SequenceSourceChain276
        self.siddhi_SequenceSourceChain274 = siddhi_SequenceSourceChain274
        self.siddhi_SequenceSourceChain278 = siddhi_SequenceSourceChain278 if siddhi_SequenceSourceChain278 is not None else set()
        self.siddhi_SequenceSourceChain649 = siddhi_SequenceSourceChain649
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def siddhi_SequenceSourceChain223(self):
        return self.__siddhi_SequenceSourceChain223

    @siddhi_SequenceSourceChain223.setter
    def siddhi_SequenceSourceChain223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain223", None)
        self.__siddhi_SequenceSourceChain223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryAbsentSequenceSourceChain222"):
                opp_val = getattr(old_value, "siddhi_EveryAbsentSequenceSourceChain222", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryAbsentSequenceSourceChain222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryAbsentSequenceSourceChain222"):
                opp_val = getattr(value, "siddhi_EveryAbsentSequenceSourceChain222", None)
                setattr(value, "siddhi_EveryAbsentSequenceSourceChain222", self)

    @property
    def siddhi_SequenceSourceChain649(self):
        return self.__siddhi_SequenceSourceChain649

    @siddhi_SequenceSourceChain649.setter
    def siddhi_SequenceSourceChain649(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain649", None)
        self.__siddhi_SequenceSourceChain649 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource1648"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource1648", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource1648", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource1648"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource1648", None)
                setattr(value, "siddhi_RightAbsentSequenceSource1648", self)

    @property
    def siddhi_SequenceSourceChain273(self):
        return self.__siddhi_SequenceSourceChain273

    @siddhi_SequenceSourceChain273.setter
    def siddhi_SequenceSourceChain273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain273", None)
        self.__siddhi_SequenceSourceChain273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SequenceSourceChain271"):
                opp_val = getattr(old_value, "siddhi_SequenceSourceChain271", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SequenceSourceChain271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SequenceSourceChain271"):
                opp_val = getattr(value, "siddhi_SequenceSourceChain271", None)
                setattr(value, "siddhi_SequenceSourceChain271", self)

    @property
    def siddhi_SequenceSourceChain278(self):
        return self.__siddhi_SequenceSourceChain278

    @siddhi_SequenceSourceChain278.setter
    def siddhi_SequenceSourceChain278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain278", None)
        self.__siddhi_SequenceSourceChain278 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "siddhi_WithinTime279"):
                    opp_val = getattr(item, "siddhi_WithinTime279", None)
                    
                    if opp_val == self:
                        setattr(item, "siddhi_WithinTime279", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "siddhi_WithinTime279"):
                    opp_val = getattr(item, "siddhi_WithinTime279", None)
                    
                    setattr(item, "siddhi_WithinTime279", self)
                    

    @property
    def siddhi_SequenceSourceChain276(self):
        return self.__siddhi_SequenceSourceChain276

    @siddhi_SequenceSourceChain276.setter
    def siddhi_SequenceSourceChain276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain276", None)
        self.__siddhi_SequenceSourceChain276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SequenceSourceChain274"):
                opp_val = getattr(old_value, "siddhi_SequenceSourceChain274", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SequenceSourceChain274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SequenceSourceChain274"):
                opp_val = getattr(value, "siddhi_SequenceSourceChain274", None)
                setattr(value, "siddhi_SequenceSourceChain274", self)

    @property
    def siddhi_SequenceSourceChain267(self):
        return self.__siddhi_SequenceSourceChain267

    @siddhi_SequenceSourceChain267.setter
    def siddhi_SequenceSourceChain267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain267", None)
        self.__siddhi_SequenceSourceChain267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource266"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource266", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource266"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource266", None)
                setattr(value, "siddhi_RightAbsentSequenceSource266", self)

    @property
    def siddhi_SequenceSourceChain274(self):
        return self.__siddhi_SequenceSourceChain274

    @siddhi_SequenceSourceChain274.setter
    def siddhi_SequenceSourceChain274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain274", None)
        self.__siddhi_SequenceSourceChain274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SequenceSourceChain276"):
                opp_val = getattr(old_value, "siddhi_SequenceSourceChain276", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SequenceSourceChain276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SequenceSourceChain276"):
                opp_val = getattr(value, "siddhi_SequenceSourceChain276", None)
                setattr(value, "siddhi_SequenceSourceChain276", self)

    @property
    def siddhi_SequenceSourceChain252(self):
        return self.__siddhi_SequenceSourceChain252

    @siddhi_SequenceSourceChain252.setter
    def siddhi_SequenceSourceChain252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain252", None)
        self.__siddhi_SequenceSourceChain252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LeftAbsentSequenceSource251"):
                opp_val = getattr(old_value, "siddhi_LeftAbsentSequenceSource251", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LeftAbsentSequenceSource251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LeftAbsentSequenceSource251"):
                opp_val = getattr(value, "siddhi_LeftAbsentSequenceSource251", None)
                setattr(value, "siddhi_LeftAbsentSequenceSource251", self)

    @property
    def siddhi_SequenceSourceChain(self):
        return self.__siddhi_SequenceSourceChain

    @siddhi_SequenceSourceChain.setter
    def siddhi_SequenceSourceChain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain", None)
        self.__siddhi_SequenceSourceChain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EverySequenceSourceChain218"):
                opp_val = getattr(old_value, "siddhi_EverySequenceSourceChain218", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EverySequenceSourceChain218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EverySequenceSourceChain218"):
                opp_val = getattr(value, "siddhi_EverySequenceSourceChain218", None)
                setattr(value, "siddhi_EverySequenceSourceChain218", self)

    @property
    def siddhi_SequenceSourceChain271(self):
        return self.__siddhi_SequenceSourceChain271

    @siddhi_SequenceSourceChain271.setter
    def siddhi_SequenceSourceChain271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_SequenceSourceChain__siddhi_SequenceSourceChain271", None)
        self.__siddhi_SequenceSourceChain271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SequenceSourceChain273"):
                opp_val = getattr(old_value, "siddhi_SequenceSourceChain273", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SequenceSourceChain273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SequenceSourceChain273"):
                opp_val = getattr(value, "siddhi_SequenceSourceChain273", None)
                setattr(value, "siddhi_SequenceSourceChain273", self)

class siddhi_WithinTime(WITHIN):

    pass
class siddhi_SequenceSource(SequenceSourceChain):

    pass
class siddhi_EveryAbsentSequenceSourceChain:

    pass
class siddhi_EverySequenceSourceChain:

    pass
class siddhi_PatternStream:

    pass
class siddhi_SequenceStream:

    pass
class siddhi_JoinStream:

    pass
class siddhi_Attribute:

    pass
class siddhi_RightAbsentSequenceSource:

    def __init__(self, comm: str, op: str, cp: str, comma: str, siddhi_RightAbsentSequenceSource: "siddhi_AbsentSequenceSourceChain" = None, siddhi_RightAbsentSequenceSource255: "siddhi_RightAbsentSequenceSource" = None, siddhi_RightAbsentSequenceSource253: "siddhi_RightAbsentSequenceSource" = None, siddhi_RightAbsentSequenceSource258: "siddhi_RightAbsentSequenceSource" = None, siddhi_RightAbsentSequenceSource256: "siddhi_RightAbsentSequenceSource" = None, siddhi_RightAbsentSequenceSource261: "siddhi_RightAbsentSequenceSource" = None, siddhi_RightAbsentSequenceSource259: "siddhi_RightAbsentSequenceSource" = None, siddhi_RightAbsentSequenceSource263: "siddhi_WithinTime" = None, siddhi_RightAbsentSequenceSource266: "siddhi_SequenceSourceChain" = None, siddhi_RightAbsentSequenceSource269: "siddhi_BasicAbsentPatternSource" = None, siddhi_RightAbsentSequenceSource646: "siddhi_RightAbsentSequenceSource1" = None):
        self.comm = comm
        self.op = op
        self.cp = cp
        self.comma = comma
        self.siddhi_RightAbsentSequenceSource = siddhi_RightAbsentSequenceSource
        self.siddhi_RightAbsentSequenceSource255 = siddhi_RightAbsentSequenceSource255
        self.siddhi_RightAbsentSequenceSource253 = siddhi_RightAbsentSequenceSource253
        self.siddhi_RightAbsentSequenceSource258 = siddhi_RightAbsentSequenceSource258
        self.siddhi_RightAbsentSequenceSource256 = siddhi_RightAbsentSequenceSource256
        self.siddhi_RightAbsentSequenceSource261 = siddhi_RightAbsentSequenceSource261
        self.siddhi_RightAbsentSequenceSource259 = siddhi_RightAbsentSequenceSource259
        self.siddhi_RightAbsentSequenceSource263 = siddhi_RightAbsentSequenceSource263
        self.siddhi_RightAbsentSequenceSource266 = siddhi_RightAbsentSequenceSource266
        self.siddhi_RightAbsentSequenceSource269 = siddhi_RightAbsentSequenceSource269
        self.siddhi_RightAbsentSequenceSource646 = siddhi_RightAbsentSequenceSource646
        
    @property
    def comm(self) -> str:
        return self.__comm

    @comm.setter
    def comm(self, comm: str):
        self.__comm = comm

    @property
    def cp(self) -> str:
        return self.__cp

    @cp.setter
    def cp(self, cp: str):
        self.__cp = cp

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def comma(self) -> str:
        return self.__comma

    @comma.setter
    def comma(self, comma: str):
        self.__comma = comma

    @property
    def siddhi_RightAbsentSequenceSource259(self):
        return self.__siddhi_RightAbsentSequenceSource259

    @siddhi_RightAbsentSequenceSource259.setter
    def siddhi_RightAbsentSequenceSource259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource259", None)
        self.__siddhi_RightAbsentSequenceSource259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource261"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource261", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource261"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource261", None)
                setattr(value, "siddhi_RightAbsentSequenceSource261", self)

    @property
    def siddhi_RightAbsentSequenceSource261(self):
        return self.__siddhi_RightAbsentSequenceSource261

    @siddhi_RightAbsentSequenceSource261.setter
    def siddhi_RightAbsentSequenceSource261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource261", None)
        self.__siddhi_RightAbsentSequenceSource261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource259"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource259", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource259"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource259", None)
                setattr(value, "siddhi_RightAbsentSequenceSource259", self)

    @property
    def siddhi_RightAbsentSequenceSource253(self):
        return self.__siddhi_RightAbsentSequenceSource253

    @siddhi_RightAbsentSequenceSource253.setter
    def siddhi_RightAbsentSequenceSource253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource253", None)
        self.__siddhi_RightAbsentSequenceSource253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource255"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource255", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource255"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource255", None)
                setattr(value, "siddhi_RightAbsentSequenceSource255", self)

    @property
    def siddhi_RightAbsentSequenceSource256(self):
        return self.__siddhi_RightAbsentSequenceSource256

    @siddhi_RightAbsentSequenceSource256.setter
    def siddhi_RightAbsentSequenceSource256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource256", None)
        self.__siddhi_RightAbsentSequenceSource256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource258"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource258", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource258"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource258", None)
                setattr(value, "siddhi_RightAbsentSequenceSource258", self)

    @property
    def siddhi_RightAbsentSequenceSource269(self):
        return self.__siddhi_RightAbsentSequenceSource269

    @siddhi_RightAbsentSequenceSource269.setter
    def siddhi_RightAbsentSequenceSource269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource269", None)
        self.__siddhi_RightAbsentSequenceSource269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_BasicAbsentPatternSource270"):
                opp_val = getattr(old_value, "siddhi_BasicAbsentPatternSource270", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_BasicAbsentPatternSource270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_BasicAbsentPatternSource270"):
                opp_val = getattr(value, "siddhi_BasicAbsentPatternSource270", None)
                setattr(value, "siddhi_BasicAbsentPatternSource270", self)

    @property
    def siddhi_RightAbsentSequenceSource646(self):
        return self.__siddhi_RightAbsentSequenceSource646

    @siddhi_RightAbsentSequenceSource646.setter
    def siddhi_RightAbsentSequenceSource646(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource646", None)
        self.__siddhi_RightAbsentSequenceSource646 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource1"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource1", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource1"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource1", None)
                setattr(value, "siddhi_RightAbsentSequenceSource1", self)

    @property
    def siddhi_RightAbsentSequenceSource258(self):
        return self.__siddhi_RightAbsentSequenceSource258

    @siddhi_RightAbsentSequenceSource258.setter
    def siddhi_RightAbsentSequenceSource258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource258", None)
        self.__siddhi_RightAbsentSequenceSource258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource256"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource256", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource256"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource256", None)
                setattr(value, "siddhi_RightAbsentSequenceSource256", self)

    @property
    def siddhi_RightAbsentSequenceSource263(self):
        return self.__siddhi_RightAbsentSequenceSource263

    @siddhi_RightAbsentSequenceSource263.setter
    def siddhi_RightAbsentSequenceSource263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource263", None)
        self.__siddhi_RightAbsentSequenceSource263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_WithinTime264"):
                opp_val = getattr(old_value, "siddhi_WithinTime264", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_WithinTime264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_WithinTime264"):
                opp_val = getattr(value, "siddhi_WithinTime264", None)
                setattr(value, "siddhi_WithinTime264", self)

    @property
    def siddhi_RightAbsentSequenceSource266(self):
        return self.__siddhi_RightAbsentSequenceSource266

    @siddhi_RightAbsentSequenceSource266.setter
    def siddhi_RightAbsentSequenceSource266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource266", None)
        self.__siddhi_RightAbsentSequenceSource266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SequenceSourceChain267"):
                opp_val = getattr(old_value, "siddhi_SequenceSourceChain267", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SequenceSourceChain267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SequenceSourceChain267"):
                opp_val = getattr(value, "siddhi_SequenceSourceChain267", None)
                setattr(value, "siddhi_SequenceSourceChain267", self)

    @property
    def siddhi_RightAbsentSequenceSource255(self):
        return self.__siddhi_RightAbsentSequenceSource255

    @siddhi_RightAbsentSequenceSource255.setter
    def siddhi_RightAbsentSequenceSource255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource255", None)
        self.__siddhi_RightAbsentSequenceSource255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_RightAbsentSequenceSource253"):
                opp_val = getattr(old_value, "siddhi_RightAbsentSequenceSource253", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_RightAbsentSequenceSource253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_RightAbsentSequenceSource253"):
                opp_val = getattr(value, "siddhi_RightAbsentSequenceSource253", None)
                setattr(value, "siddhi_RightAbsentSequenceSource253", self)

    @property
    def siddhi_RightAbsentSequenceSource(self):
        return self.__siddhi_RightAbsentSequenceSource

    @siddhi_RightAbsentSequenceSource.setter
    def siddhi_RightAbsentSequenceSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_RightAbsentSequenceSource__siddhi_RightAbsentSequenceSource", None)
        self.__siddhi_RightAbsentSequenceSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_AbsentSequenceSourceChain235"):
                opp_val = getattr(old_value, "siddhi_AbsentSequenceSourceChain235", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_AbsentSequenceSourceChain235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_AbsentSequenceSourceChain235"):
                opp_val = getattr(value, "siddhi_AbsentSequenceSourceChain235", None)
                setattr(value, "siddhi_AbsentSequenceSourceChain235", self)

class HAVING:

    pass
class GROUP:

    pass
class siddhi_HavingExpr(HAVING):

    pass
class siddhi_OutputAttribute:

    pass
class SELECT:

    pass
class FIRST:

    pass
class LAST:

    pass
class siddhi_AttributeIndex(LAST):

    pass
class SNAPSHOT:

    pass
class CURRENT:

    pass
class EXPIRED:

    pass
class RAW:

    pass
class EVENTS:

    pass
class ALL:

    pass
class siddhi_OutputRateType(LAST, FIRST, ALL):

    pass
class siddhi_SetAssignment:

    pass
class siddhi_ON:

    def __init__(self, on: str, siddhi_ON: "siddhi_QueryOutput" = None, siddhi_ON421: "siddhi_JoinStream" = None, siddhi_ON621: "siddhi_Keyword" = None):
        self.on = on
        self.siddhi_ON = siddhi_ON
        self.siddhi_ON421 = siddhi_ON421
        self.siddhi_ON621 = siddhi_ON621
        
    @property
    def on(self) -> str:
        return self.__on

    @on.setter
    def on(self, on: str):
        self.__on = on

    @property
    def siddhi_ON621(self):
        return self.__siddhi_ON621

    @siddhi_ON621.setter
    def siddhi_ON621(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ON__siddhi_ON621", None)
        self.__siddhi_ON621 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Keyword620"):
                opp_val = getattr(old_value, "siddhi_Keyword620", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Keyword620", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Keyword620"):
                opp_val = getattr(value, "siddhi_Keyword620", None)
                setattr(value, "siddhi_Keyword620", self)

    @property
    def siddhi_ON421(self):
        return self.__siddhi_ON421

    @siddhi_ON421.setter
    def siddhi_ON421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ON__siddhi_ON421", None)
        self.__siddhi_ON421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_JoinStream420"):
                opp_val = getattr(old_value, "siddhi_JoinStream420", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_JoinStream420", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_JoinStream420"):
                opp_val = getattr(value, "siddhi_JoinStream420", None)
                setattr(value, "siddhi_JoinStream420", self)

    @property
    def siddhi_ON(self):
        return self.__siddhi_ON

    @siddhi_ON.setter
    def siddhi_ON(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_ON__siddhi_ON", None)
        self.__siddhi_ON = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_QueryOutput151"):
                opp_val = getattr(old_value, "siddhi_QueryOutput151", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_QueryOutput151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_QueryOutput151"):
                opp_val = getattr(value, "siddhi_QueryOutput151", None)
                setattr(value, "siddhi_QueryOutput151", self)

class siddhi_Target:

    pass
class UPDATE:

    pass
class FOR:

    pass
class siddhi_ForTime(FOR):

    pass
class DELETE:

    pass
class INTO:

    pass
class INSERT:

    pass
class siddhi_QuerySection:

    pass
class siddhi_QueryInput:

    pass
class siddhi_AS:

    def __init__(self, a: str, siddhi_AS: "siddhi_ConditionRange" = None, siddhi_AS200: "siddhi_OutAttr" = None, siddhi_AS451: "siddhi_MainSource" = None, siddhi_AS612: "siddhi_Keyword" = None):
        self.a = a
        self.siddhi_AS = siddhi_AS
        self.siddhi_AS200 = siddhi_AS200
        self.siddhi_AS451 = siddhi_AS451
        self.siddhi_AS612 = siddhi_AS612
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def siddhi_AS200(self):
        return self.__siddhi_AS200

    @siddhi_AS200.setter
    def siddhi_AS200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AS__siddhi_AS200", None)
        self.__siddhi_AS200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_OutAttr199"):
                opp_val = getattr(old_value, "siddhi_OutAttr199", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_OutAttr199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_OutAttr199"):
                opp_val = getattr(value, "siddhi_OutAttr199", None)
                setattr(value, "siddhi_OutAttr199", self)

    @property
    def siddhi_AS612(self):
        return self.__siddhi_AS612

    @siddhi_AS612.setter
    def siddhi_AS612(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AS__siddhi_AS612", None)
        self.__siddhi_AS612 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Keyword"):
                opp_val = getattr(old_value, "siddhi_Keyword", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Keyword", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Keyword"):
                opp_val = getattr(value, "siddhi_Keyword", None)
                setattr(value, "siddhi_Keyword", self)

    @property
    def siddhi_AS(self):
        return self.__siddhi_AS

    @siddhi_AS.setter
    def siddhi_AS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AS__siddhi_AS", None)
        self.__siddhi_AS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_ConditionRange130"):
                opp_val = getattr(old_value, "siddhi_ConditionRange130", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_ConditionRange130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_ConditionRange130"):
                opp_val = getattr(value, "siddhi_ConditionRange130", None)
                setattr(value, "siddhi_ConditionRange130", self)

    @property
    def siddhi_AS451(self):
        return self.__siddhi_AS451

    @siddhi_AS451.setter
    def siddhi_AS451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AS__siddhi_AS451", None)
        self.__siddhi_AS451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MainSource450"):
                opp_val = getattr(old_value, "siddhi_MainSource450", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MainSource450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MainSource450"):
                opp_val = getattr(value, "siddhi_MainSource450", None)
                setattr(value, "siddhi_MainSource450", self)

class siddhi_Expression:

    pass
class SET:

    pass
class siddhi_SetClause(SET):

    pass
class siddhi_OR:

    def __init__(self, or: str, siddhi_OR: "siddhi_ConditionRanges" = None, siddhi_OR157: "siddhi_QueryOutput" = None, siddhi_OR340: "siddhi_LogicalStatefulSource" = None, siddhi_OR365: "siddhi_LogicalAbsentStatefulSource" = None, siddhi_OR627: "siddhi_Keyword" = None, siddhi_OR659: "siddhi_MathLogicalOperation" = None):
        self.or = or
        self.siddhi_OR = siddhi_OR
        self.siddhi_OR157 = siddhi_OR157
        self.siddhi_OR340 = siddhi_OR340
        self.siddhi_OR365 = siddhi_OR365
        self.siddhi_OR627 = siddhi_OR627
        self.siddhi_OR659 = siddhi_OR659
        
    @property
    def or(self) -> str:
        return self.__or

    @or.setter
    def or(self, or: str):
        self.__or = or

    @property
    def siddhi_OR659(self):
        return self.__siddhi_OR659

    @siddhi_OR659.setter
    def siddhi_OR659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_OR__siddhi_OR659", None)
        self.__siddhi_OR659 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathLogicalOperation658"):
                opp_val = getattr(old_value, "siddhi_MathLogicalOperation658", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathLogicalOperation658", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathLogicalOperation658"):
                opp_val = getattr(value, "siddhi_MathLogicalOperation658", None)
                setattr(value, "siddhi_MathLogicalOperation658", self)

    @property
    def siddhi_OR157(self):
        return self.__siddhi_OR157

    @siddhi_OR157.setter
    def siddhi_OR157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_OR__siddhi_OR157", None)
        self.__siddhi_OR157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_QueryOutput156"):
                opp_val = getattr(old_value, "siddhi_QueryOutput156", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_QueryOutput156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_QueryOutput156"):
                opp_val = getattr(value, "siddhi_QueryOutput156", None)
                setattr(value, "siddhi_QueryOutput156", self)

    @property
    def siddhi_OR(self):
        return self.__siddhi_OR

    @siddhi_OR.setter
    def siddhi_OR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_OR__siddhi_OR", None)
        self.__siddhi_OR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_ConditionRanges126"):
                opp_val = getattr(old_value, "siddhi_ConditionRanges126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_ConditionRanges126"):
                opp_val = getattr(value, "siddhi_ConditionRanges126", None)
                if opp_val is None:
                    setattr(value, "siddhi_ConditionRanges126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def siddhi_OR365(self):
        return self.__siddhi_OR365

    @siddhi_OR365.setter
    def siddhi_OR365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_OR__siddhi_OR365", None)
        self.__siddhi_OR365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LogicalAbsentStatefulSource364"):
                opp_val = getattr(old_value, "siddhi_LogicalAbsentStatefulSource364", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LogicalAbsentStatefulSource364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LogicalAbsentStatefulSource364"):
                opp_val = getattr(value, "siddhi_LogicalAbsentStatefulSource364", None)
                setattr(value, "siddhi_LogicalAbsentStatefulSource364", self)

    @property
    def siddhi_OR340(self):
        return self.__siddhi_OR340

    @siddhi_OR340.setter
    def siddhi_OR340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_OR__siddhi_OR340", None)
        self.__siddhi_OR340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LogicalStatefulSource339"):
                opp_val = getattr(old_value, "siddhi_LogicalStatefulSource339", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LogicalStatefulSource339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LogicalStatefulSource339"):
                opp_val = getattr(value, "siddhi_LogicalStatefulSource339", None)
                setattr(value, "siddhi_LogicalStatefulSource339", self)

    @property
    def siddhi_OR627(self):
        return self.__siddhi_OR627

    @siddhi_OR627.setter
    def siddhi_OR627(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_OR__siddhi_OR627", None)
        self.__siddhi_OR627 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Keyword626"):
                opp_val = getattr(old_value, "siddhi_Keyword626", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Keyword626", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Keyword626"):
                opp_val = getattr(value, "siddhi_Keyword626", None)
                setattr(value, "siddhi_Keyword626", self)

class siddhi_ConditionRange:

    pass
class siddhi_OF:

    def __init__(self, of: str, siddhi_OF: "siddhi_ConditionRanges" = None, siddhi_OF633: "siddhi_Keyword" = None):
        self.of = of
        self.siddhi_OF = siddhi_OF
        self.siddhi_OF633 = siddhi_OF633
        
    @property
    def of(self) -> str:
        return self.__of

    @of.setter
    def of(self, of: str):
        self.__of = of

    @property
    def siddhi_OF(self):
        return self.__siddhi_OF

    @siddhi_OF.setter
    def siddhi_OF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_OF__siddhi_OF", None)
        self.__siddhi_OF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_ConditionRanges"):
                opp_val = getattr(old_value, "siddhi_ConditionRanges", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_ConditionRanges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_ConditionRanges"):
                opp_val = getattr(value, "siddhi_ConditionRanges", None)
                setattr(value, "siddhi_ConditionRanges", self)

    @property
    def siddhi_OF633(self):
        return self.__siddhi_OF633

    @siddhi_OF633.setter
    def siddhi_OF633(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_OF__siddhi_OF633", None)
        self.__siddhi_OF633 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Keyword632"):
                opp_val = getattr(old_value, "siddhi_Keyword632", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Keyword632", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Keyword632"):
                opp_val = getattr(value, "siddhi_Keyword632", None)
                setattr(value, "siddhi_Keyword632", self)

class PartitionWithStream:

    pass
class siddhi_ConditionRanges(PartitionWithStream):

    pass
class siddhi_PartitionWithStream:

    pass
class END:

    pass
class BEGIN:

    pass
class WITH:

    pass
class PARTITION:

    pass
class Source1OrStandardStatefulSource:

    pass
class siddhi_StreamAlias(Source1OrStandardStatefulSource):

    pass
class siddhi_StandardStatefulSource(SequenceSource, SequenceCollectionStatefulSource, Source1OrStandardStatefulSource, PatternCollectionStatefulSource):

    def __init__(self, zero_or_more: str, zero_or_one: str, one_or_more: str, siddhi_StandardStatefulSource: "siddhi_PatternSource" = None, siddhi_StandardStatefulSource335: "siddhi_LogicalStatefulSource" = None, siddhi_StandardStatefulSource346: "siddhi_LogicalAbsentStatefulSource" = None, siddhi_StandardStatefulSource535: "siddhi_Collect" = None, siddhi_StandardStatefulSource537: "siddhi_Source" = None, siddhi_StandardStatefulSource540: "siddhi_BasicSourceStreamHandlers" = None):
        self.zero_or_more = zero_or_more
        self.zero_or_one = zero_or_one
        self.one_or_more = one_or_more
        self.siddhi_StandardStatefulSource = siddhi_StandardStatefulSource
        self.siddhi_StandardStatefulSource335 = siddhi_StandardStatefulSource335
        self.siddhi_StandardStatefulSource346 = siddhi_StandardStatefulSource346
        self.siddhi_StandardStatefulSource535 = siddhi_StandardStatefulSource535
        self.siddhi_StandardStatefulSource537 = siddhi_StandardStatefulSource537
        self.siddhi_StandardStatefulSource540 = siddhi_StandardStatefulSource540
        
    @property
    def zero_or_more(self) -> str:
        return self.__zero_or_more

    @zero_or_more.setter
    def zero_or_more(self, zero_or_more: str):
        self.__zero_or_more = zero_or_more

    @property
    def zero_or_one(self) -> str:
        return self.__zero_or_one

    @zero_or_one.setter
    def zero_or_one(self, zero_or_one: str):
        self.__zero_or_one = zero_or_one

    @property
    def one_or_more(self) -> str:
        return self.__one_or_more

    @one_or_more.setter
    def one_or_more(self, one_or_more: str):
        self.__one_or_more = one_or_more

    @property
    def siddhi_StandardStatefulSource537(self):
        return self.__siddhi_StandardStatefulSource537

    @siddhi_StandardStatefulSource537.setter
    def siddhi_StandardStatefulSource537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StandardStatefulSource__siddhi_StandardStatefulSource537", None)
        self.__siddhi_StandardStatefulSource537 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Source538"):
                opp_val = getattr(old_value, "siddhi_Source538", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Source538", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Source538"):
                opp_val = getattr(value, "siddhi_Source538", None)
                setattr(value, "siddhi_Source538", self)

    @property
    def siddhi_StandardStatefulSource346(self):
        return self.__siddhi_StandardStatefulSource346

    @siddhi_StandardStatefulSource346.setter
    def siddhi_StandardStatefulSource346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StandardStatefulSource__siddhi_StandardStatefulSource346", None)
        self.__siddhi_StandardStatefulSource346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LogicalAbsentStatefulSource345"):
                opp_val = getattr(old_value, "siddhi_LogicalAbsentStatefulSource345", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_LogicalAbsentStatefulSource345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LogicalAbsentStatefulSource345"):
                opp_val = getattr(value, "siddhi_LogicalAbsentStatefulSource345", None)
                setattr(value, "siddhi_LogicalAbsentStatefulSource345", self)

    @property
    def siddhi_StandardStatefulSource540(self):
        return self.__siddhi_StandardStatefulSource540

    @siddhi_StandardStatefulSource540.setter
    def siddhi_StandardStatefulSource540(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StandardStatefulSource__siddhi_StandardStatefulSource540", None)
        self.__siddhi_StandardStatefulSource540 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_BasicSourceStreamHandlers541"):
                opp_val = getattr(old_value, "siddhi_BasicSourceStreamHandlers541", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_BasicSourceStreamHandlers541", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_BasicSourceStreamHandlers541"):
                opp_val = getattr(value, "siddhi_BasicSourceStreamHandlers541", None)
                setattr(value, "siddhi_BasicSourceStreamHandlers541", self)

    @property
    def siddhi_StandardStatefulSource(self):
        return self.__siddhi_StandardStatefulSource

    @siddhi_StandardStatefulSource.setter
    def siddhi_StandardStatefulSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StandardStatefulSource__siddhi_StandardStatefulSource", None)
        self.__siddhi_StandardStatefulSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PatternSource330"):
                opp_val = getattr(old_value, "siddhi_PatternSource330", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PatternSource330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PatternSource330"):
                opp_val = getattr(value, "siddhi_PatternSource330", None)
                setattr(value, "siddhi_PatternSource330", self)

    @property
    def siddhi_StandardStatefulSource535(self):
        return self.__siddhi_StandardStatefulSource535

    @siddhi_StandardStatefulSource535.setter
    def siddhi_StandardStatefulSource535(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StandardStatefulSource__siddhi_StandardStatefulSource535", None)
        self.__siddhi_StandardStatefulSource535 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Collect"):
                opp_val = getattr(old_value, "siddhi_Collect", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Collect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Collect"):
                opp_val = getattr(value, "siddhi_Collect", None)
                setattr(value, "siddhi_Collect", self)

    @property
    def siddhi_StandardStatefulSource335(self):
        return self.__siddhi_StandardStatefulSource335

    @siddhi_StandardStatefulSource335.setter
    def siddhi_StandardStatefulSource335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StandardStatefulSource__siddhi_StandardStatefulSource335", None)
        self.__siddhi_StandardStatefulSource335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_LogicalStatefulSource334"):
                opp_val = getattr(old_value, "siddhi_LogicalStatefulSource334", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_LogicalStatefulSource334"):
                opp_val = getattr(value, "siddhi_LogicalStatefulSource334", None)
                if opp_val is None:
                    setattr(value, "siddhi_LogicalStatefulSource334", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class siddhi_Source:

    pass
class OBJECT:

    pass
class BOOL:

    pass
class DOUBLE:

    pass
class FLOAT:

    pass
class LONG:

    pass
class INTS:

    pass
class STRINGS:

    pass
class FeaturesOrOutAttr:

    pass
class siddhi_OutAttr(FeaturesOrOutAttr):

    pass
class siddhi_PropertySeparator:

    pass
class siddhi_PropertyValue:

    pass
class siddhi_PropertyName:

    pass
class siddhi_AnnotationElement:

    pass
class siddhi_Name:

    def __init__(self, na: str, siddhi_Name: "siddhi_Annotation" = None, siddhi_Name100: "siddhi_PropertyName" = None, siddhi_Name105: "siddhi_Features" = None, siddhi_Name444: "siddhi_StreamAlias" = None, siddhi_Name505: "siddhi_StreamReference" = None, siddhi_Name574: "siddhi_FunctionNamespace" = None, siddhi_Name577: "siddhi_FunctionId" = None, siddhi_Name641: "siddhi_APP" = None, siddhi_Name666: "siddhi_MathInOperation" = None):
        self.na = na
        self.siddhi_Name = siddhi_Name
        self.siddhi_Name100 = siddhi_Name100
        self.siddhi_Name105 = siddhi_Name105
        self.siddhi_Name444 = siddhi_Name444
        self.siddhi_Name505 = siddhi_Name505
        self.siddhi_Name574 = siddhi_Name574
        self.siddhi_Name577 = siddhi_Name577
        self.siddhi_Name641 = siddhi_Name641
        self.siddhi_Name666 = siddhi_Name666
        
    @property
    def na(self) -> str:
        return self.__na

    @na.setter
    def na(self, na: str):
        self.__na = na

    @property
    def siddhi_Name641(self):
        return self.__siddhi_Name641

    @siddhi_Name641.setter
    def siddhi_Name641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name641", None)
        self.__siddhi_Name641 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_APP"):
                opp_val = getattr(old_value, "siddhi_APP", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_APP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_APP"):
                opp_val = getattr(value, "siddhi_APP", None)
                setattr(value, "siddhi_APP", self)

    @property
    def siddhi_Name(self):
        return self.__siddhi_Name

    @siddhi_Name.setter
    def siddhi_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name", None)
        self.__siddhi_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Annotation85"):
                opp_val = getattr(old_value, "siddhi_Annotation85", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Annotation85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Annotation85"):
                opp_val = getattr(value, "siddhi_Annotation85", None)
                setattr(value, "siddhi_Annotation85", self)

    @property
    def siddhi_Name105(self):
        return self.__siddhi_Name105

    @siddhi_Name105.setter
    def siddhi_Name105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name105", None)
        self.__siddhi_Name105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Features104"):
                opp_val = getattr(old_value, "siddhi_Features104", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Features104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Features104"):
                opp_val = getattr(value, "siddhi_Features104", None)
                setattr(value, "siddhi_Features104", self)

    @property
    def siddhi_Name577(self):
        return self.__siddhi_Name577

    @siddhi_Name577.setter
    def siddhi_Name577(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name577", None)
        self.__siddhi_Name577 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_FunctionId576"):
                opp_val = getattr(old_value, "siddhi_FunctionId576", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_FunctionId576", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_FunctionId576"):
                opp_val = getattr(value, "siddhi_FunctionId576", None)
                setattr(value, "siddhi_FunctionId576", self)

    @property
    def siddhi_Name666(self):
        return self.__siddhi_Name666

    @siddhi_Name666.setter
    def siddhi_Name666(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name666", None)
        self.__siddhi_Name666 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_MathInOperation665"):
                opp_val = getattr(old_value, "siddhi_MathInOperation665", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_MathInOperation665", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_MathInOperation665"):
                opp_val = getattr(value, "siddhi_MathInOperation665", None)
                setattr(value, "siddhi_MathInOperation665", self)

    @property
    def siddhi_Name574(self):
        return self.__siddhi_Name574

    @siddhi_Name574.setter
    def siddhi_Name574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name574", None)
        self.__siddhi_Name574 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_FunctionNamespace573"):
                opp_val = getattr(old_value, "siddhi_FunctionNamespace573", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_FunctionNamespace573", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_FunctionNamespace573"):
                opp_val = getattr(value, "siddhi_FunctionNamespace573", None)
                setattr(value, "siddhi_FunctionNamespace573", self)

    @property
    def siddhi_Name100(self):
        return self.__siddhi_Name100

    @siddhi_Name100.setter
    def siddhi_Name100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name100", None)
        self.__siddhi_Name100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PropertyName99"):
                opp_val = getattr(old_value, "siddhi_PropertyName99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PropertyName99"):
                opp_val = getattr(value, "siddhi_PropertyName99", None)
                if opp_val is None:
                    setattr(value, "siddhi_PropertyName99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def siddhi_Name444(self):
        return self.__siddhi_Name444

    @siddhi_Name444.setter
    def siddhi_Name444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name444", None)
        self.__siddhi_Name444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_StreamAlias"):
                opp_val = getattr(old_value, "siddhi_StreamAlias", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_StreamAlias", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_StreamAlias"):
                opp_val = getattr(value, "siddhi_StreamAlias", None)
                setattr(value, "siddhi_StreamAlias", self)

    @property
    def siddhi_Name505(self):
        return self.__siddhi_Name505

    @siddhi_Name505.setter
    def siddhi_Name505(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Name__siddhi_Name505", None)
        self.__siddhi_Name505 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_StreamReference504"):
                opp_val = getattr(old_value, "siddhi_StreamReference504", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_StreamReference504", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_StreamReference504"):
                opp_val = getattr(value, "siddhi_StreamReference504", None)
                setattr(value, "siddhi_StreamReference504", self)

class YEARS:

    pass
class siddhi_YearValue(YEARS):

    pass
class MONTHS:

    pass
class siddhi_MonthValue(MONTHS):

    pass
class WEEKS:

    pass
class siddhi_WeekValue(WEEKS):

    pass
class DAYS:

    pass
class siddhi_DayValue(DAYS):

    pass
class HOURS:

    pass
class siddhi_HourValue(HOURS):

    pass
class MINUTES:

    pass
class siddhi_MinuteValue(MINUTES):

    pass
class SECONDS:

    pass
class siddhi_SecondValue(SECONDS):

    pass
class AggregationTime:

    pass
class siddhi_AggregationTimeRange(AggregationTime):

    pass
class siddhi_AggregationTimeInterval(AggregationTime):

    pass
class siddhi_AggregationTimeDuration(HOURS, YEARS, SECONDS, WEEKS, MINUTES, MONTHS, DAYS):

    pass
class siddhi_AggregationTime:

    pass
class siddhi_AttributeReference(SetAssignment):

    def __init__(self, name: str, hash1: str, hash2: str, siddhi_AttributeReference: "siddhi_DefinitionAggregation" = None, siddhi_AttributeReference187: "siddhi_GroupBy" = None, siddhi_AttributeReference195: "siddhi_OutputAttribute" = None, siddhi_AttributeReference499: "siddhi_NullCheck" = None, siddhi_AttributeReference515: "siddhi_Literal" = None, siddhi_AttributeReference517: "siddhi_Expression" = None, siddhi_AttributeReference520: "siddhi_SourceOrEventReference" = None, siddhi_AttributeReference522: "siddhi_AttributeIndex" = None, siddhi_AttributeReference525: "siddhi_SourceOrEventReference" = None, siddhi_AttributeReference528: "siddhi_AttributeIndex" = None, siddhi_AttributeReference531: "siddhi_FeaturesOrOutAttrReference" = None):
        self.name = name
        self.hash1 = hash1
        self.hash2 = hash2
        self.siddhi_AttributeReference = siddhi_AttributeReference
        self.siddhi_AttributeReference187 = siddhi_AttributeReference187
        self.siddhi_AttributeReference195 = siddhi_AttributeReference195
        self.siddhi_AttributeReference499 = siddhi_AttributeReference499
        self.siddhi_AttributeReference515 = siddhi_AttributeReference515
        self.siddhi_AttributeReference517 = siddhi_AttributeReference517
        self.siddhi_AttributeReference520 = siddhi_AttributeReference520
        self.siddhi_AttributeReference522 = siddhi_AttributeReference522
        self.siddhi_AttributeReference525 = siddhi_AttributeReference525
        self.siddhi_AttributeReference528 = siddhi_AttributeReference528
        self.siddhi_AttributeReference531 = siddhi_AttributeReference531
        
    @property
    def hash1(self) -> str:
        return self.__hash1

    @hash1.setter
    def hash1(self, hash1: str):
        self.__hash1 = hash1

    @property
    def hash2(self) -> str:
        return self.__hash2

    @hash2.setter
    def hash2(self, hash2: str):
        self.__hash2 = hash2

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def siddhi_AttributeReference531(self):
        return self.__siddhi_AttributeReference531

    @siddhi_AttributeReference531.setter
    def siddhi_AttributeReference531(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference531", None)
        self.__siddhi_AttributeReference531 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_FeaturesOrOutAttrReference"):
                opp_val = getattr(old_value, "siddhi_FeaturesOrOutAttrReference", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_FeaturesOrOutAttrReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_FeaturesOrOutAttrReference"):
                opp_val = getattr(value, "siddhi_FeaturesOrOutAttrReference", None)
                setattr(value, "siddhi_FeaturesOrOutAttrReference", self)

    @property
    def siddhi_AttributeReference522(self):
        return self.__siddhi_AttributeReference522

    @siddhi_AttributeReference522.setter
    def siddhi_AttributeReference522(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference522", None)
        self.__siddhi_AttributeReference522 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_AttributeIndex523"):
                opp_val = getattr(old_value, "siddhi_AttributeIndex523", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_AttributeIndex523", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_AttributeIndex523"):
                opp_val = getattr(value, "siddhi_AttributeIndex523", None)
                setattr(value, "siddhi_AttributeIndex523", self)

    @property
    def siddhi_AttributeReference(self):
        return self.__siddhi_AttributeReference

    @siddhi_AttributeReference.setter
    def siddhi_AttributeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference", None)
        self.__siddhi_AttributeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionAggregation76"):
                opp_val = getattr(old_value, "siddhi_DefinitionAggregation76", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionAggregation76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionAggregation76"):
                opp_val = getattr(value, "siddhi_DefinitionAggregation76", None)
                setattr(value, "siddhi_DefinitionAggregation76", self)

    @property
    def siddhi_AttributeReference515(self):
        return self.__siddhi_AttributeReference515

    @siddhi_AttributeReference515.setter
    def siddhi_AttributeReference515(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference515", None)
        self.__siddhi_AttributeReference515 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Literal514"):
                opp_val = getattr(old_value, "siddhi_Literal514", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Literal514", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Literal514"):
                opp_val = getattr(value, "siddhi_Literal514", None)
                setattr(value, "siddhi_Literal514", self)

    @property
    def siddhi_AttributeReference520(self):
        return self.__siddhi_AttributeReference520

    @siddhi_AttributeReference520.setter
    def siddhi_AttributeReference520(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference520", None)
        self.__siddhi_AttributeReference520 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SourceOrEventReference"):
                opp_val = getattr(old_value, "siddhi_SourceOrEventReference", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SourceOrEventReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SourceOrEventReference"):
                opp_val = getattr(value, "siddhi_SourceOrEventReference", None)
                setattr(value, "siddhi_SourceOrEventReference", self)

    @property
    def siddhi_AttributeReference517(self):
        return self.__siddhi_AttributeReference517

    @siddhi_AttributeReference517.setter
    def siddhi_AttributeReference517(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference517", None)
        self.__siddhi_AttributeReference517 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Expression518"):
                opp_val = getattr(old_value, "siddhi_Expression518", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Expression518", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Expression518"):
                opp_val = getattr(value, "siddhi_Expression518", None)
                setattr(value, "siddhi_Expression518", self)

    @property
    def siddhi_AttributeReference187(self):
        return self.__siddhi_AttributeReference187

    @siddhi_AttributeReference187.setter
    def siddhi_AttributeReference187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference187", None)
        self.__siddhi_AttributeReference187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_GroupBy186"):
                opp_val = getattr(old_value, "siddhi_GroupBy186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_GroupBy186"):
                opp_val = getattr(value, "siddhi_GroupBy186", None)
                if opp_val is None:
                    setattr(value, "siddhi_GroupBy186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def siddhi_AttributeReference525(self):
        return self.__siddhi_AttributeReference525

    @siddhi_AttributeReference525.setter
    def siddhi_AttributeReference525(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference525", None)
        self.__siddhi_AttributeReference525 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_SourceOrEventReference526"):
                opp_val = getattr(old_value, "siddhi_SourceOrEventReference526", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_SourceOrEventReference526", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_SourceOrEventReference526"):
                opp_val = getattr(value, "siddhi_SourceOrEventReference526", None)
                setattr(value, "siddhi_SourceOrEventReference526", self)

    @property
    def siddhi_AttributeReference528(self):
        return self.__siddhi_AttributeReference528

    @siddhi_AttributeReference528.setter
    def siddhi_AttributeReference528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference528", None)
        self.__siddhi_AttributeReference528 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_AttributeIndex529"):
                opp_val = getattr(old_value, "siddhi_AttributeIndex529", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_AttributeIndex529", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_AttributeIndex529"):
                opp_val = getattr(value, "siddhi_AttributeIndex529", None)
                setattr(value, "siddhi_AttributeIndex529", self)

    @property
    def siddhi_AttributeReference499(self):
        return self.__siddhi_AttributeReference499

    @siddhi_AttributeReference499.setter
    def siddhi_AttributeReference499(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference499", None)
        self.__siddhi_AttributeReference499 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_NullCheck498"):
                opp_val = getattr(old_value, "siddhi_NullCheck498", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_NullCheck498", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_NullCheck498"):
                opp_val = getattr(value, "siddhi_NullCheck498", None)
                setattr(value, "siddhi_NullCheck498", self)

    @property
    def siddhi_AttributeReference195(self):
        return self.__siddhi_AttributeReference195

    @siddhi_AttributeReference195.setter
    def siddhi_AttributeReference195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_AttributeReference__siddhi_AttributeReference195", None)
        self.__siddhi_AttributeReference195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_OutputAttribute194"):
                opp_val = getattr(old_value, "siddhi_OutputAttribute194", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_OutputAttribute194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_OutputAttribute194"):
                opp_val = getattr(value, "siddhi_OutputAttribute194", None)
                setattr(value, "siddhi_OutputAttribute194", self)

class siddhi_GroupByQuerySelection(SELECT):

    pass
class siddhi_StandardStream(JoinStream):

    pass
class BY:

    pass
class siddhi_GroupBy(GROUP, BY):

    pass
class AGGREGATE:

    pass
class FROM:

    pass
class AGGREGATION:

    pass
class siddhi_FunctionBody:

    def __init__(self, value: str, siddhi_FunctionBody: "siddhi_DefinitionFunction" = None):
        self.value = value
        self.siddhi_FunctionBody = siddhi_FunctionBody
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def siddhi_FunctionBody(self):
        return self.__siddhi_FunctionBody

    @siddhi_FunctionBody.setter
    def siddhi_FunctionBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_FunctionBody__siddhi_FunctionBody", None)
        self.__siddhi_FunctionBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionFunction64"):
                opp_val = getattr(old_value, "siddhi_DefinitionFunction64", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionFunction64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionFunction64"):
                opp_val = getattr(value, "siddhi_DefinitionFunction64", None)
                setattr(value, "siddhi_DefinitionFunction64", self)

class siddhi_LanguageName:

    def __init__(self, id: str, siddhi_LanguageName: "siddhi_DefinitionFunction" = None):
        self.id = id
        self.siddhi_LanguageName = siddhi_LanguageName
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def siddhi_LanguageName(self):
        return self.__siddhi_LanguageName

    @siddhi_LanguageName.setter
    def siddhi_LanguageName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_LanguageName__siddhi_LanguageName", None)
        self.__siddhi_LanguageName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionFunction60"):
                opp_val = getattr(old_value, "siddhi_DefinitionFunction60", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionFunction60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionFunction60"):
                opp_val = getattr(value, "siddhi_DefinitionFunction60", None)
                setattr(value, "siddhi_DefinitionFunction60", self)

class siddhi_FunctionName:

    def __init__(self, id: str, siddhi_FunctionName: "siddhi_DefinitionFunction" = None):
        self.id = id
        self.siddhi_FunctionName = siddhi_FunctionName
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def siddhi_FunctionName(self):
        return self.__siddhi_FunctionName

    @siddhi_FunctionName.setter
    def siddhi_FunctionName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_FunctionName__siddhi_FunctionName", None)
        self.__siddhi_FunctionName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionFunction58"):
                opp_val = getattr(old_value, "siddhi_DefinitionFunction58", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionFunction58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionFunction58"):
                opp_val = getattr(value, "siddhi_DefinitionFunction58", None)
                setattr(value, "siddhi_DefinitionFunction58", self)

class RETURN:

    pass
class siddhi_QueryOutput(DELETE, UPDATE, FOR, INSERT, INTO, RETURN):

    pass
class siddhi_AnonymousStream(RETURN, FROM):

    pass
class FUNCTION:

    pass
class siddhi_StringValue:

    def __init__(self, sl: str, siddhi_StringValue: "siddhi_DefinitionTrigger" = None, siddhi_StringValue97: "siddhi_PropertyValue" = None, siddhi_StringValue133: "siddhi_ConditionRange" = None, siddhi_StringValue565: "siddhi_ConstantValue" = None):
        self.sl = sl
        self.siddhi_StringValue = siddhi_StringValue
        self.siddhi_StringValue97 = siddhi_StringValue97
        self.siddhi_StringValue133 = siddhi_StringValue133
        self.siddhi_StringValue565 = siddhi_StringValue565
        
    @property
    def sl(self) -> str:
        return self.__sl

    @sl.setter
    def sl(self, sl: str):
        self.__sl = sl

    @property
    def siddhi_StringValue565(self):
        return self.__siddhi_StringValue565

    @siddhi_StringValue565.setter
    def siddhi_StringValue565(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StringValue__siddhi_StringValue565", None)
        self.__siddhi_StringValue565 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_ConstantValue564"):
                opp_val = getattr(old_value, "siddhi_ConstantValue564", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_ConstantValue564", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_ConstantValue564"):
                opp_val = getattr(value, "siddhi_ConstantValue564", None)
                setattr(value, "siddhi_ConstantValue564", self)

    @property
    def siddhi_StringValue133(self):
        return self.__siddhi_StringValue133

    @siddhi_StringValue133.setter
    def siddhi_StringValue133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StringValue__siddhi_StringValue133", None)
        self.__siddhi_StringValue133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_ConditionRange132"):
                opp_val = getattr(old_value, "siddhi_ConditionRange132", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_ConditionRange132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_ConditionRange132"):
                opp_val = getattr(value, "siddhi_ConditionRange132", None)
                setattr(value, "siddhi_ConditionRange132", self)

    @property
    def siddhi_StringValue(self):
        return self.__siddhi_StringValue

    @siddhi_StringValue.setter
    def siddhi_StringValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StringValue__siddhi_StringValue", None)
        self.__siddhi_StringValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionTrigger56"):
                opp_val = getattr(old_value, "siddhi_DefinitionTrigger56", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionTrigger56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionTrigger56"):
                opp_val = getattr(value, "siddhi_DefinitionTrigger56", None)
                setattr(value, "siddhi_DefinitionTrigger56", self)

    @property
    def siddhi_StringValue97(self):
        return self.__siddhi_StringValue97

    @siddhi_StringValue97.setter
    def siddhi_StringValue97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_StringValue__siddhi_StringValue97", None)
        self.__siddhi_StringValue97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_PropertyValue96"):
                opp_val = getattr(old_value, "siddhi_PropertyValue96", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_PropertyValue96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_PropertyValue96"):
                opp_val = getattr(value, "siddhi_PropertyValue96", None)
                setattr(value, "siddhi_PropertyValue96", self)

class siddhi_TimeValue:

    pass
class siddhi_EVERY(EveryAbsentSequenceSourceChain, AbsentPatternSourceChain, RightAbsentPatternSource, EveryAbsentPatternSource, LeftAbsentPatternSource, EverySequenceSourceChain):

    def __init__(self, every1: str, siddhi_EVERY: "siddhi_DefinitionTrigger" = None, siddhi_EVERY79: "siddhi_DefinitionAggregation" = None, siddhi_EVERY172: "siddhi_OutputRate" = None, siddhi_EVERY310: "siddhi_EveryPatternSourceChain" = None, siddhi_EVERY615: "siddhi_Keyword" = None):
        self.every1 = every1
        self.siddhi_EVERY = siddhi_EVERY
        self.siddhi_EVERY79 = siddhi_EVERY79
        self.siddhi_EVERY172 = siddhi_EVERY172
        self.siddhi_EVERY310 = siddhi_EVERY310
        self.siddhi_EVERY615 = siddhi_EVERY615
        
    @property
    def every1(self) -> str:
        return self.__every1

    @every1.setter
    def every1(self, every1: str):
        self.__every1 = every1

    @property
    def siddhi_EVERY172(self):
        return self.__siddhi_EVERY172

    @siddhi_EVERY172.setter
    def siddhi_EVERY172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EVERY__siddhi_EVERY172", None)
        self.__siddhi_EVERY172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_OutputRate171"):
                opp_val = getattr(old_value, "siddhi_OutputRate171", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_OutputRate171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_OutputRate171"):
                opp_val = getattr(value, "siddhi_OutputRate171", None)
                setattr(value, "siddhi_OutputRate171", self)

    @property
    def siddhi_EVERY79(self):
        return self.__siddhi_EVERY79

    @siddhi_EVERY79.setter
    def siddhi_EVERY79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EVERY__siddhi_EVERY79", None)
        self.__siddhi_EVERY79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionAggregation78"):
                opp_val = getattr(old_value, "siddhi_DefinitionAggregation78", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionAggregation78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionAggregation78"):
                opp_val = getattr(value, "siddhi_DefinitionAggregation78", None)
                setattr(value, "siddhi_DefinitionAggregation78", self)

    @property
    def siddhi_EVERY615(self):
        return self.__siddhi_EVERY615

    @siddhi_EVERY615.setter
    def siddhi_EVERY615(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EVERY__siddhi_EVERY615", None)
        self.__siddhi_EVERY615 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Keyword614"):
                opp_val = getattr(old_value, "siddhi_Keyword614", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Keyword614", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Keyword614"):
                opp_val = getattr(value, "siddhi_Keyword614", None)
                setattr(value, "siddhi_Keyword614", self)

    @property
    def siddhi_EVERY(self):
        return self.__siddhi_EVERY

    @siddhi_EVERY.setter
    def siddhi_EVERY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EVERY__siddhi_EVERY", None)
        self.__siddhi_EVERY = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionTrigger52"):
                opp_val = getattr(old_value, "siddhi_DefinitionTrigger52", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionTrigger52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionTrigger52"):
                opp_val = getattr(value, "siddhi_DefinitionTrigger52", None)
                setattr(value, "siddhi_DefinitionTrigger52", self)

    @property
    def siddhi_EVERY310(self):
        return self.__siddhi_EVERY310

    @siddhi_EVERY310.setter
    def siddhi_EVERY310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_EVERY__siddhi_EVERY310", None)
        self.__siddhi_EVERY310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_EveryPatternSourceChain309"):
                opp_val = getattr(old_value, "siddhi_EveryPatternSourceChain309", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_EveryPatternSourceChain309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_EveryPatternSourceChain309"):
                opp_val = getattr(value, "siddhi_EveryPatternSourceChain309", None)
                setattr(value, "siddhi_EveryPatternSourceChain309", self)

class siddhi_TriggerName:

    def __init__(self, id: str, siddhi_TriggerName: "siddhi_DefinitionTrigger" = None):
        self.id = id
        self.siddhi_TriggerName = siddhi_TriggerName
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def siddhi_TriggerName(self):
        return self.__siddhi_TriggerName

    @siddhi_TriggerName.setter
    def siddhi_TriggerName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_TriggerName__siddhi_TriggerName", None)
        self.__siddhi_TriggerName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionTrigger50"):
                opp_val = getattr(old_value, "siddhi_DefinitionTrigger50", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionTrigger50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionTrigger50"):
                opp_val = getattr(value, "siddhi_DefinitionTrigger50", None)
                setattr(value, "siddhi_DefinitionTrigger50", self)

class AT:

    pass
class TRIGGER:

    pass
class siddhi_OutputEventType(RAW, EVENTS, ALL, EXPIRED, CURRENT):

    pass
class siddhi_FunctionOperation:

    pass
class siddhi_AttributeType(STRINGS, OBJECT, BOOL, FLOAT, DOUBLE, LONG, INTS):

    pass
class OUTPUT:

    pass
class siddhi_OutputRate(EVENTS, SNAPSHOT, OUTPUT):

    pass
class WINDOW:

    pass
class siddhi_BasicSourceStreamHandlers1(WINDOW):

    pass
class siddhi_Win(WINDOW):

    pass
class TABLE:

    pass
class siddhi_Features(FeaturesOrOutAttr):

    pass
class siddhi_Source1(Source1OrStandardStatefulSource):

    def __init__(self, inner: str, siddhi_Source1: "siddhi_DefinitionStream" = None, siddhi_Source132: "siddhi_DefinitionTable" = None, siddhi_Source141: "siddhi_DefinitionWindow" = None, siddhi_Source170: "siddhi_DefinitionAggregation" = None, siddhi_Source1110: "siddhi_Source" = None, siddhi_Source1162: "siddhi_Target" = None):
        self.inner = inner
        self.siddhi_Source1 = siddhi_Source1
        self.siddhi_Source132 = siddhi_Source132
        self.siddhi_Source141 = siddhi_Source141
        self.siddhi_Source170 = siddhi_Source170
        self.siddhi_Source1110 = siddhi_Source1110
        self.siddhi_Source1162 = siddhi_Source1162
        
    @property
    def inner(self) -> str:
        return self.__inner

    @inner.setter
    def inner(self, inner: str):
        self.__inner = inner

    @property
    def siddhi_Source141(self):
        return self.__siddhi_Source141

    @siddhi_Source141.setter
    def siddhi_Source141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Source1__siddhi_Source141", None)
        self.__siddhi_Source141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionWindow40"):
                opp_val = getattr(old_value, "siddhi_DefinitionWindow40", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionWindow40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionWindow40"):
                opp_val = getattr(value, "siddhi_DefinitionWindow40", None)
                setattr(value, "siddhi_DefinitionWindow40", self)

    @property
    def siddhi_Source1(self):
        return self.__siddhi_Source1

    @siddhi_Source1.setter
    def siddhi_Source1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Source1__siddhi_Source1", None)
        self.__siddhi_Source1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionStream24"):
                opp_val = getattr(old_value, "siddhi_DefinitionStream24", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionStream24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionStream24"):
                opp_val = getattr(value, "siddhi_DefinitionStream24", None)
                setattr(value, "siddhi_DefinitionStream24", self)

    @property
    def siddhi_Source1162(self):
        return self.__siddhi_Source1162

    @siddhi_Source1162.setter
    def siddhi_Source1162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Source1__siddhi_Source1162", None)
        self.__siddhi_Source1162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Target161"):
                opp_val = getattr(old_value, "siddhi_Target161", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Target161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Target161"):
                opp_val = getattr(value, "siddhi_Target161", None)
                setattr(value, "siddhi_Target161", self)

    @property
    def siddhi_Source170(self):
        return self.__siddhi_Source170

    @siddhi_Source170.setter
    def siddhi_Source170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Source1__siddhi_Source170", None)
        self.__siddhi_Source170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionAggregation69"):
                opp_val = getattr(old_value, "siddhi_DefinitionAggregation69", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionAggregation69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionAggregation69"):
                opp_val = getattr(value, "siddhi_DefinitionAggregation69", None)
                setattr(value, "siddhi_DefinitionAggregation69", self)

    @property
    def siddhi_Source132(self):
        return self.__siddhi_Source132

    @siddhi_Source132.setter
    def siddhi_Source132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Source1__siddhi_Source132", None)
        self.__siddhi_Source132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_DefinitionTable31"):
                opp_val = getattr(old_value, "siddhi_DefinitionTable31", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_DefinitionTable31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_DefinitionTable31"):
                opp_val = getattr(value, "siddhi_DefinitionTable31", None)
                setattr(value, "siddhi_DefinitionTable31", self)

    @property
    def siddhi_Source1110(self):
        return self.__siddhi_Source1110

    @siddhi_Source1110.setter
    def siddhi_Source1110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siddhi_Source1__siddhi_Source1110", None)
        self.__siddhi_Source1110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siddhi_Source"):
                opp_val = getattr(old_value, "siddhi_Source", None)
                if opp_val == self:
                    setattr(old_value, "siddhi_Source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siddhi_Source"):
                opp_val = getattr(value, "siddhi_Source", None)
                setattr(value, "siddhi_Source", self)

class siddhi_Annotation:

    pass
class STREAM:

    pass
class DEFINE:

    pass
class siddhi_Keyword(LAST, YEARS, SECONDS, Name, INNER, DEFINE, HAVING, NULL, CURRENT, RIGHT, STREAM, HOURS, IS, WINDOW, PARTITION, TABLE, INTO, SNAPSHOT, WITH, GROUP, BEGIN, MILLISECONDS, EVENTS, FIRST, OBJECT, DELETE, FALSE, WEEKS, OUTER, FOR, WITHIN, FLOAT, INSERT, DOUBLE, INTS, SELECT, MINUTES, END, FROM, RAW, LEFT, ALL, STRINGS, UPDATE, BOOL, OUTPUT, JOIN, EXPIRED, FULL, LONG, TRUE, BY, MONTHS, RETURN, DAYS):

    pass
class siddhi_Query(FROM):

    pass
class siddhi_ExecPartition(BEGIN, END, PARTITION, WITH):

    pass
class siddhi_DefinitionFunction(RETURN, FUNCTION, DEFINE):

    pass
class siddhi_DefinitionTrigger(AT, TRIGGER, DEFINE):

    pass
class siddhi_DefinitionWindow(DEFINE, OUTPUT, WINDOW):

    pass
class siddhi_DefinitionTable(TABLE, DEFINE):

    pass
class siddhi_DefinitionStream(DEFINE, STREAM):

    pass
class siddhi_AppAnnotation:

    pass
class siddhi_ExecutionPlan:

    pass
class siddhi_SiddhiQL:

    pass
class siddhi_ExecutionElement:

    pass
class siddhi_DefinitionAggregation(DEFINE, AGGREGATE, BY, AGGREGATION, FROM):

    pass