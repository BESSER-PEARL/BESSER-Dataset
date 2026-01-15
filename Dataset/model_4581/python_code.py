from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Action:

    pass
class sparrow_Callprocess(Action):

    def __init__(self, target: str, source: str, datasource: str, value: str):
        self.target = target
        self.source = source
        self.datasource = datasource
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def datasource(self) -> str:
        return self.__datasource

    @datasource.setter
    def datasource(self, datasource: str):
        self.__datasource = datasource

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

class sparrow_Fetch(Action):

    def __init__(self, source: str, value: str):
        self.source = source
        self.value = value
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sparrow_Sms(Action):

    def __init__(self, target: str, value: str):
        self.target = target
        self.value = value
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sparrow_Transform(Action):

    def __init__(self, on: str, value: str):
        self.on = on
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def on(self) -> str:
        return self.__on

    @on.setter
    def on(self, on: str):
        self.__on = on

class sparrow_SlackPUT(Action):

    def __init__(self, team: str, channel: str, value: str):
        self.team = team
        self.channel = channel
        self.value = value
        
    @property
    def team(self) -> str:
        return self.__team

    @team.setter
    def team(self, team: str):
        self.__team = team

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def channel(self) -> str:
        return self.__channel

    @channel.setter
    def channel(self, channel: str):
        self.__channel = channel

class sparrow_WriteCsv(Action):

    def __init__(self, source: str, to: str, delim: str, value: str):
        self.source = source
        self.to = to
        self.delim = delim
        self.value = value
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def delim(self) -> str:
        return self.__delim

    @delim.setter
    def delim(self, delim: str):
        self.__delim = delim

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

class sparrow_TrelloPUT(Action):

    def __init__(self, authtoken: str, key: str, useraccount: str, list: str, source: str, value: str):
        self.authtoken = authtoken
        self.key = key
        self.useraccount = useraccount
        self.list = list
        self.source = source
        self.value = value
        
    @property
    def useraccount(self) -> str:
        return self.__useraccount

    @useraccount.setter
    def useraccount(self, useraccount: str):
        self.__useraccount = useraccount

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def authtoken(self) -> str:
        return self.__authtoken

    @authtoken.setter
    def authtoken(self, authtoken: str):
        self.__authtoken = authtoken

    @property
    def list(self) -> str:
        return self.__list

    @list.setter
    def list(self, list: str):
        self.__list = list

class sparrow_LoadCsv(Action):

    def __init__(self, source: str, to: str, delim: str, value: str):
        self.source = source
        self.to = to
        self.delim = delim
        self.value = value
        
    @property
    def delim(self) -> str:
        return self.__delim

    @delim.setter
    def delim(self, delim: str):
        self.__delim = delim

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

class sparrow_Updatedaudit(Action):

    def __init__(self, value: str, logsink: str):
        self.value = value
        self.logsink = logsink
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def logsink(self) -> str:
        return self.__logsink

    @logsink.setter
    def logsink(self, logsink: str):
        self.__logsink = logsink

class sparrow_Dropfile(Action):

    def __init__(self, target: str):
        self.target = target
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class sparrow_GooglecalPUT(Action):

    def __init__(self, authstore: str, key: str, useraccount: str, source: str, value: str):
        self.authstore = authstore
        self.key = key
        self.useraccount = useraccount
        self.source = source
        self.value = value
        
    @property
    def useraccount(self) -> str:
        return self.__useraccount

    @useraccount.setter
    def useraccount(self, useraccount: str):
        self.__useraccount = useraccount

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def authstore(self) -> str:
        return self.__authstore

    @authstore.setter
    def authstore(self, authstore: str):
        self.__authstore = authstore

class sparrow_TrelloGET(Action):

    def __init__(self, authtoken: str, key: str, useraccount: str, board: str, target: str, value: str):
        self.authtoken = authtoken
        self.key = key
        self.useraccount = useraccount
        self.board = board
        self.target = target
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def useraccount(self) -> str:
        return self.__useraccount

    @useraccount.setter
    def useraccount(self, useraccount: str):
        self.__useraccount = useraccount

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def board(self) -> str:
        return self.__board

    @board.setter
    def board(self, board: str):
        self.__board = board

    @property
    def authtoken(self) -> str:
        return self.__authtoken

    @authtoken.setter
    def authtoken(self, authtoken: str):
        self.__authtoken = authtoken

class sparrow_Copydata(Action):

    def __init__(self, source: str, to: str, value: str):
        self.source = source
        self.to = to
        self.value = value
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

class sparrow_FBCLead(Action):

    def __init__(self, accessToken: str, appSecret: str, accountId: str, campaignId: str, target: str, value: str):
        self.accessToken = accessToken
        self.appSecret = appSecret
        self.accountId = accountId
        self.campaignId = campaignId
        self.target = target
        self.value = value
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def accountId(self) -> str:
        return self.__accountId

    @accountId.setter
    def accountId(self, accountId: str):
        self.__accountId = accountId

    @property
    def campaignId(self) -> str:
        return self.__campaignId

    @campaignId.setter
    def campaignId(self, campaignId: str):
        self.__campaignId = campaignId

    @property
    def accessToken(self) -> str:
        return self.__accessToken

    @accessToken.setter
    def accessToken(self, accessToken: str):
        self.__accessToken = accessToken

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def appSecret(self) -> str:
        return self.__appSecret

    @appSecret.setter
    def appSecret(self, appSecret: str):
        self.__appSecret = appSecret

class sparrow_Expression:

    def __init__(self, lhs: str, operator: str, rhs: str, sparrow_Expression: "sparrow_Action" = None):
        self.lhs = lhs
        self.operator = operator
        self.rhs = rhs
        self.sparrow_Expression = sparrow_Expression
        
    @property
    def rhs(self) -> str:
        return self.__rhs

    @rhs.setter
    def rhs(self, rhs: str):
        self.__rhs = rhs

    @property
    def lhs(self) -> str:
        return self.__lhs

    @lhs.setter
    def lhs(self, lhs: str):
        self.__lhs = lhs

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def sparrow_Expression(self):
        return self.__sparrow_Expression

    @sparrow_Expression.setter
    def sparrow_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Expression__sparrow_Expression", None)
        self.__sparrow_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Action14"):
                opp_val = getattr(old_value, "sparrow_Action14", None)
                if opp_val == self:
                    setattr(old_value, "sparrow_Action14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Action14"):
                opp_val = getattr(value, "sparrow_Action14", None)
                setattr(value, "sparrow_Action14", self)

class sparrow_Action:

    def __init__(self, name: str, sparrow_Action: "sparrow_Try" = None, sparrow_Action9: "sparrow_Finally" = None, sparrow_Action12: "sparrow_Catch" = None, sparrow_Action14: "sparrow_Expression" = None):
        self.name = name
        self.sparrow_Action = sparrow_Action
        self.sparrow_Action9 = sparrow_Action9
        self.sparrow_Action12 = sparrow_Action12
        self.sparrow_Action14 = sparrow_Action14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sparrow_Action(self):
        return self.__sparrow_Action

    @sparrow_Action.setter
    def sparrow_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Action__sparrow_Action", None)
        self.__sparrow_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Try6"):
                opp_val = getattr(old_value, "sparrow_Try6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Try6"):
                opp_val = getattr(value, "sparrow_Try6", None)
                if opp_val is None:
                    setattr(value, "sparrow_Try6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sparrow_Action9(self):
        return self.__sparrow_Action9

    @sparrow_Action9.setter
    def sparrow_Action9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Action__sparrow_Action9", None)
        self.__sparrow_Action9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Finally8"):
                opp_val = getattr(old_value, "sparrow_Finally8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Finally8"):
                opp_val = getattr(value, "sparrow_Finally8", None)
                if opp_val is None:
                    setattr(value, "sparrow_Finally8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sparrow_Action14(self):
        return self.__sparrow_Action14

    @sparrow_Action14.setter
    def sparrow_Action14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Action__sparrow_Action14", None)
        self.__sparrow_Action14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Expression"):
                opp_val = getattr(old_value, "sparrow_Expression", None)
                if opp_val == self:
                    setattr(old_value, "sparrow_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Expression"):
                opp_val = getattr(value, "sparrow_Expression", None)
                setattr(value, "sparrow_Expression", self)

    @property
    def sparrow_Action12(self):
        return self.__sparrow_Action12

    @sparrow_Action12.setter
    def sparrow_Action12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Action__sparrow_Action12", None)
        self.__sparrow_Action12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Catch11"):
                opp_val = getattr(old_value, "sparrow_Catch11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Catch11"):
                opp_val = getattr(value, "sparrow_Catch11", None)
                if opp_val is None:
                    setattr(value, "sparrow_Catch11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sparrow_RestPart:

    def __init__(self, partName: str, partData: str, sparrow_RestPart: "sparrow_Rest" = None):
        self.partName = partName
        self.partData = partData
        self.sparrow_RestPart = sparrow_RestPart
        
    @property
    def partName(self) -> str:
        return self.__partName

    @partName.setter
    def partName(self, partName: str):
        self.__partName = partName

    @property
    def partData(self) -> str:
        return self.__partData

    @partData.setter
    def partData(self, partData: str):
        self.__partData = partData

    @property
    def sparrow_RestPart(self):
        return self.__sparrow_RestPart

    @sparrow_RestPart.setter
    def sparrow_RestPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_RestPart__sparrow_RestPart", None)
        self.__sparrow_RestPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Rest"):
                opp_val = getattr(old_value, "sparrow_Rest", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Rest"):
                opp_val = getattr(value, "sparrow_Rest", None)
                if opp_val is None:
                    setattr(value, "sparrow_Rest", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sparrow_Rest(Action):

    def __init__(self, authtoken: str, url: str, method: str, resourcedatafrom: str, urldata: str, headerdatafrom: str, headerdata: str, postdatafrom: str, parentName: str, parentdata: str, ackdatato: str, ackdata: str, sparrow_Rest: set["sparrow_RestPart"] = None):
        self.authtoken = authtoken
        self.url = url
        self.method = method
        self.resourcedatafrom = resourcedatafrom
        self.urldata = urldata
        self.headerdatafrom = headerdatafrom
        self.headerdata = headerdata
        self.postdatafrom = postdatafrom
        self.parentName = parentName
        self.parentdata = parentdata
        self.ackdatato = ackdatato
        self.ackdata = ackdata
        self.sparrow_Rest = sparrow_Rest if sparrow_Rest is not None else set()
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def headerdatafrom(self) -> str:
        return self.__headerdatafrom

    @headerdatafrom.setter
    def headerdatafrom(self, headerdatafrom: str):
        self.__headerdatafrom = headerdatafrom

    @property
    def parentName(self) -> str:
        return self.__parentName

    @parentName.setter
    def parentName(self, parentName: str):
        self.__parentName = parentName

    @property
    def postdatafrom(self) -> str:
        return self.__postdatafrom

    @postdatafrom.setter
    def postdatafrom(self, postdatafrom: str):
        self.__postdatafrom = postdatafrom

    @property
    def resourcedatafrom(self) -> str:
        return self.__resourcedatafrom

    @resourcedatafrom.setter
    def resourcedatafrom(self, resourcedatafrom: str):
        self.__resourcedatafrom = resourcedatafrom

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def headerdata(self) -> str:
        return self.__headerdata

    @headerdata.setter
    def headerdata(self, headerdata: str):
        self.__headerdata = headerdata

    @property
    def authtoken(self) -> str:
        return self.__authtoken

    @authtoken.setter
    def authtoken(self, authtoken: str):
        self.__authtoken = authtoken

    @property
    def ackdata(self) -> str:
        return self.__ackdata

    @ackdata.setter
    def ackdata(self, ackdata: str):
        self.__ackdata = ackdata

    @property
    def parentdata(self) -> str:
        return self.__parentdata

    @parentdata.setter
    def parentdata(self, parentdata: str):
        self.__parentdata = parentdata

    @property
    def urldata(self) -> str:
        return self.__urldata

    @urldata.setter
    def urldata(self, urldata: str):
        self.__urldata = urldata

    @property
    def ackdatato(self) -> str:
        return self.__ackdatato

    @ackdatato.setter
    def ackdatato(self, ackdatato: str):
        self.__ackdatato = ackdatato

    @property
    def sparrow_Rest(self):
        return self.__sparrow_Rest

    @sparrow_Rest.setter
    def sparrow_Rest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Rest__sparrow_Rest", None)
        self.__sparrow_Rest = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sparrow_RestPart"):
                    opp_val = getattr(item, "sparrow_RestPart", None)
                    
                    if opp_val == self:
                        setattr(item, "sparrow_RestPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sparrow_RestPart"):
                    opp_val = getattr(item, "sparrow_RestPart", None)
                    
                    setattr(item, "sparrow_RestPart", self)
                    

class sparrow_Doozle(Action):

    def __init__(self, target: str, on: str, value: str):
        self.target = target
        self.on = on
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def on(self) -> str:
        return self.__on

    @on.setter
    def on(self, on: str):
        self.__on = on

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class sparrow_Finally:

    def __init__(self, name: str, sparrow_Finally: "sparrow_Process" = None, sparrow_Finally8: set["sparrow_Action"] = None):
        self.name = name
        self.sparrow_Finally = sparrow_Finally
        self.sparrow_Finally8 = sparrow_Finally8 if sparrow_Finally8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sparrow_Finally8(self):
        return self.__sparrow_Finally8

    @sparrow_Finally8.setter
    def sparrow_Finally8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Finally__sparrow_Finally8", None)
        self.__sparrow_Finally8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sparrow_Action9"):
                    opp_val = getattr(item, "sparrow_Action9", None)
                    
                    if opp_val == self:
                        setattr(item, "sparrow_Action9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sparrow_Action9"):
                    opp_val = getattr(item, "sparrow_Action9", None)
                    
                    setattr(item, "sparrow_Action9", self)
                    

    @property
    def sparrow_Finally(self):
        return self.__sparrow_Finally

    @sparrow_Finally.setter
    def sparrow_Finally(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Finally__sparrow_Finally", None)
        self.__sparrow_Finally = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Process4"):
                opp_val = getattr(old_value, "sparrow_Process4", None)
                if opp_val == self:
                    setattr(old_value, "sparrow_Process4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Process4"):
                opp_val = getattr(value, "sparrow_Process4", None)
                setattr(value, "sparrow_Process4", self)

class sparrow_Catch:

    def __init__(self, name: str, sparrow_Catch: "sparrow_Process" = None, sparrow_Catch11: set["sparrow_Action"] = None):
        self.name = name
        self.sparrow_Catch = sparrow_Catch
        self.sparrow_Catch11 = sparrow_Catch11 if sparrow_Catch11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sparrow_Catch11(self):
        return self.__sparrow_Catch11

    @sparrow_Catch11.setter
    def sparrow_Catch11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Catch__sparrow_Catch11", None)
        self.__sparrow_Catch11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sparrow_Action12"):
                    opp_val = getattr(item, "sparrow_Action12", None)
                    
                    if opp_val == self:
                        setattr(item, "sparrow_Action12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sparrow_Action12"):
                    opp_val = getattr(item, "sparrow_Action12", None)
                    
                    setattr(item, "sparrow_Action12", self)
                    

    @property
    def sparrow_Catch(self):
        return self.__sparrow_Catch

    @sparrow_Catch.setter
    def sparrow_Catch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Catch__sparrow_Catch", None)
        self.__sparrow_Catch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Process2"):
                opp_val = getattr(old_value, "sparrow_Process2", None)
                if opp_val == self:
                    setattr(old_value, "sparrow_Process2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Process2"):
                opp_val = getattr(value, "sparrow_Process2", None)
                setattr(value, "sparrow_Process2", self)

class sparrow_Try:

    def __init__(self, name: str, sparrow_Try: "sparrow_Process" = None, sparrow_Try6: set["sparrow_Action"] = None):
        self.name = name
        self.sparrow_Try = sparrow_Try
        self.sparrow_Try6 = sparrow_Try6 if sparrow_Try6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sparrow_Try6(self):
        return self.__sparrow_Try6

    @sparrow_Try6.setter
    def sparrow_Try6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Try__sparrow_Try6", None)
        self.__sparrow_Try6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sparrow_Action"):
                    opp_val = getattr(item, "sparrow_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "sparrow_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sparrow_Action"):
                    opp_val = getattr(item, "sparrow_Action", None)
                    
                    setattr(item, "sparrow_Action", self)
                    

    @property
    def sparrow_Try(self):
        return self.__sparrow_Try

    @sparrow_Try.setter
    def sparrow_Try(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Try__sparrow_Try", None)
        self.__sparrow_Try = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Process"):
                opp_val = getattr(old_value, "sparrow_Process", None)
                if opp_val == self:
                    setattr(old_value, "sparrow_Process", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Process"):
                opp_val = getattr(value, "sparrow_Process", None)
                setattr(value, "sparrow_Process", self)

class sparrow_Process:

    def __init__(self, name: str, sparrow_Process: "sparrow_Try" = None, sparrow_Process2: "sparrow_Catch" = None, sparrow_Process4: "sparrow_Finally" = None):
        self.name = name
        self.sparrow_Process = sparrow_Process
        self.sparrow_Process2 = sparrow_Process2
        self.sparrow_Process4 = sparrow_Process4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sparrow_Process(self):
        return self.__sparrow_Process

    @sparrow_Process.setter
    def sparrow_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Process__sparrow_Process", None)
        self.__sparrow_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Try"):
                opp_val = getattr(old_value, "sparrow_Try", None)
                if opp_val == self:
                    setattr(old_value, "sparrow_Try", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Try"):
                opp_val = getattr(value, "sparrow_Try", None)
                setattr(value, "sparrow_Try", self)

    @property
    def sparrow_Process2(self):
        return self.__sparrow_Process2

    @sparrow_Process2.setter
    def sparrow_Process2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Process__sparrow_Process2", None)
        self.__sparrow_Process2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Catch"):
                opp_val = getattr(old_value, "sparrow_Catch", None)
                if opp_val == self:
                    setattr(old_value, "sparrow_Catch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Catch"):
                opp_val = getattr(value, "sparrow_Catch", None)
                setattr(value, "sparrow_Catch", self)

    @property
    def sparrow_Process4(self):
        return self.__sparrow_Process4

    @sparrow_Process4.setter
    def sparrow_Process4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparrow_Process__sparrow_Process4", None)
        self.__sparrow_Process4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparrow_Finally"):
                opp_val = getattr(old_value, "sparrow_Finally", None)
                if opp_val == self:
                    setattr(old_value, "sparrow_Finally", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparrow_Finally"):
                opp_val = getattr(value, "sparrow_Finally", None)
                setattr(value, "sparrow_Finally", self)
