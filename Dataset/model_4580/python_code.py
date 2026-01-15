from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dsl_RestPart:

    def __init__(self, partName: str, partData: str, dsl_RestPart: "dsl_Rest" = None):
        self.partName = partName
        self.partData = partData
        self.dsl_RestPart = dsl_RestPart
        
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
    def dsl_RestPart(self):
        return self.__dsl_RestPart

    @dsl_RestPart.setter
    def dsl_RestPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_RestPart__dsl_RestPart", None)
        self.__dsl_RestPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Rest"):
                opp_val = getattr(old_value, "dsl_Rest", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Rest"):
                opp_val = getattr(value, "dsl_Rest", None)
                if opp_val is None:
                    setattr(value, "dsl_Rest", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Action:

    pass
class dsl_Abort(Action):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dsl_LoadCsv(Action):

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

class dsl_FBCLead(Action):

    def __init__(self, accessToken: str, appSecret: str, accountId: str, campaignId: str, target: str, value: str):
        self.accessToken = accessToken
        self.appSecret = appSecret
        self.accountId = accountId
        self.campaignId = campaignId
        self.target = target
        self.value = value
        
    @property
    def accessToken(self) -> str:
        return self.__accessToken

    @accessToken.setter
    def accessToken(self, accessToken: str):
        self.__accessToken = accessToken

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def campaignId(self) -> str:
        return self.__campaignId

    @campaignId.setter
    def campaignId(self, campaignId: str):
        self.__campaignId = campaignId

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def accountId(self) -> str:
        return self.__accountId

    @accountId.setter
    def accountId(self, accountId: str):
        self.__accountId = accountId

    @property
    def appSecret(self) -> str:
        return self.__appSecret

    @appSecret.setter
    def appSecret(self, appSecret: str):
        self.__appSecret = appSecret

class dsl_GooglecontactPUT(Action):

    def __init__(self, account: str, privateKey: str, ptwelveFile: str, project: str, impersonatedUser: str, dbSrc: str, value: str):
        self.account = account
        self.privateKey = privateKey
        self.ptwelveFile = ptwelveFile
        self.project = project
        self.impersonatedUser = impersonatedUser
        self.dbSrc = dbSrc
        self.value = value
        
    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, account: str):
        self.__account = account

    @property
    def impersonatedUser(self) -> str:
        return self.__impersonatedUser

    @impersonatedUser.setter
    def impersonatedUser(self, impersonatedUser: str):
        self.__impersonatedUser = impersonatedUser

    @property
    def dbSrc(self) -> str:
        return self.__dbSrc

    @dbSrc.setter
    def dbSrc(self, dbSrc: str):
        self.__dbSrc = dbSrc

    @property
    def ptwelveFile(self) -> str:
        return self.__ptwelveFile

    @ptwelveFile.setter
    def ptwelveFile(self, ptwelveFile: str):
        self.__ptwelveFile = ptwelveFile

class dsl_SendMail(Action):

    def __init__(self, impersonatedUser: str, dbSrc: str, value: str, dryrunMail: str, privateKey: str):
        self.impersonatedUser = impersonatedUser
        self.dbSrc = dbSrc
        self.value = value
        self.dryrunMail = dryrunMail
        self.privateKey = privateKey
        
    @property
    def dbSrc(self) -> str:
        return self.__dbSrc

    @dbSrc.setter
    def dbSrc(self, dbSrc: str):
        self.__dbSrc = dbSrc

    @property
    def impersonatedUser(self) -> str:
        return self.__impersonatedUser

    @impersonatedUser.setter
    def impersonatedUser(self, impersonatedUser: str):
        self.__impersonatedUser = impersonatedUser

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def dryrunMail(self) -> str:
        return self.__dryrunMail

    @dryrunMail.setter
    def dryrunMail(self, dryrunMail: str):
        self.__dryrunMail = dryrunMail

class dsl_Rest(Action):

    def __init__(self, urldata: str, headerdatafrom: str, headerdata: str, postdatafrom: str, parentName: str, parentdata: str, ackdatato: str, ackdata: str, authtoken: str, url: str, method: str, resourcedatafrom: str, dsl_Rest: set["dsl_RestPart"] = None):
        self.urldata = urldata
        self.headerdatafrom = headerdatafrom
        self.headerdata = headerdata
        self.postdatafrom = postdatafrom
        self.parentName = parentName
        self.parentdata = parentdata
        self.ackdatato = ackdatato
        self.ackdata = ackdata
        self.authtoken = authtoken
        self.url = url
        self.method = method
        self.resourcedatafrom = resourcedatafrom
        self.dsl_Rest = dsl_Rest if dsl_Rest is not None else set()
        
    @property
    def parentName(self) -> str:
        return self.__parentName

    @parentName.setter
    def parentName(self, parentName: str):
        self.__parentName = parentName

    @property
    def headerdatafrom(self) -> str:
        return self.__headerdatafrom

    @headerdatafrom.setter
    def headerdatafrom(self, headerdatafrom: str):
        self.__headerdatafrom = headerdatafrom

    @property
    def postdatafrom(self) -> str:
        return self.__postdatafrom

    @postdatafrom.setter
    def postdatafrom(self, postdatafrom: str):
        self.__postdatafrom = postdatafrom

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def ackdata(self) -> str:
        return self.__ackdata

    @ackdata.setter
    def ackdata(self, ackdata: str):
        self.__ackdata = ackdata

    @property
    def resourcedatafrom(self) -> str:
        return self.__resourcedatafrom

    @resourcedatafrom.setter
    def resourcedatafrom(self, resourcedatafrom: str):
        self.__resourcedatafrom = resourcedatafrom

    @property
    def headerdata(self) -> str:
        return self.__headerdata

    @headerdata.setter
    def headerdata(self, headerdata: str):
        self.__headerdata = headerdata

    @property
    def parentdata(self) -> str:
        return self.__parentdata

    @parentdata.setter
    def parentdata(self, parentdata: str):
        self.__parentdata = parentdata

    @property
    def authtoken(self) -> str:
        return self.__authtoken

    @authtoken.setter
    def authtoken(self, authtoken: str):
        self.__authtoken = authtoken

    @property
    def ackdatato(self) -> str:
        return self.__ackdatato

    @ackdatato.setter
    def ackdatato(self, ackdatato: str):
        self.__ackdatato = ackdatato

    @property
    def urldata(self) -> str:
        return self.__urldata

    @urldata.setter
    def urldata(self, urldata: str):
        self.__urldata = urldata

    @property
    def dsl_Rest(self):
        return self.__dsl_Rest

    @dsl_Rest.setter
    def dsl_Rest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Rest__dsl_Rest", None)
        self.__dsl_Rest = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_RestPart"):
                    opp_val = getattr(item, "dsl_RestPart", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_RestPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_RestPart"):
                    opp_val = getattr(item, "dsl_RestPart", None)
                    
                    setattr(item, "dsl_RestPart", self)
                    

class dsl_WriteCsv(Action):

    def __init__(self, source: str, to: str, delim: str, value: str):
        self.source = source
        self.to = to
        self.delim = delim
        self.value = value
        
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

class dsl_Updatedaudit(Action):

    def __init__(self, logsink: str, datasource: str, value: str):
        self.logsink = logsink
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
    def logsink(self) -> str:
        return self.__logsink

    @logsink.setter
    def logsink(self, logsink: str):
        self.__logsink = logsink

class dsl_FBFormDownload(Action):

    def __init__(self, accessToken: str, appSecret: str, accountId: str, formId: str, target: str, value: str):
        self.accessToken = accessToken
        self.appSecret = appSecret
        self.accountId = accountId
        self.formId = formId
        self.target = target
        self.value = value
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def accessToken(self) -> str:
        return self.__accessToken

    @accessToken.setter
    def accessToken(self, accessToken: str):
        self.__accessToken = accessToken

    @property
    def accountId(self) -> str:
        return self.__accountId

    @accountId.setter
    def accountId(self, accountId: str):
        self.__accountId = accountId

    @property
    def appSecret(self) -> str:
        return self.__appSecret

    @appSecret.setter
    def appSecret(self, appSecret: str):
        self.__appSecret = appSecret

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def formId(self) -> str:
        return self.__formId

    @formId.setter
    def formId(self, formId: str):
        self.__formId = formId

class dsl_Callprocess(Action):

    def __init__(self, target: str, source: str, datasource: str, value: str):
        self.target = target
        self.source = source
        self.datasource = datasource
        self.value = value
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

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

    @property
    def datasource(self) -> str:
        return self.__datasource

    @datasource.setter
    def datasource(self, datasource: str):
        self.__datasource = datasource

class dsl_TrelloGET(Action):

    def __init__(self, authtoken: str, key: str, useraccount: str, board: str, target: str, value: str):
        self.authtoken = authtoken
        self.key = key
        self.useraccount = useraccount
        self.board = board
        self.target = target
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
    def authtoken(self) -> str:
        return self.__authtoken

    @authtoken.setter
    def authtoken(self, authtoken: str):
        self.__authtoken = authtoken

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def board(self) -> str:
        return self.__board

    @board.setter
    def board(self, board: str):
        self.__board = board

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class dsl_TrelloPUT(Action):

    def __init__(self, authtoken: str, key: str, useraccount: str, list: str, source: str, value: str):
        self.authtoken = authtoken
        self.key = key
        self.useraccount = useraccount
        self.list = list
        self.source = source
        self.value = value
        
    @property
    def authtoken(self) -> str:
        return self.__authtoken

    @authtoken.setter
    def authtoken(self, authtoken: str):
        self.__authtoken = authtoken

    @property
    def useraccount(self) -> str:
        return self.__useraccount

    @useraccount.setter
    def useraccount(self, useraccount: str):
        self.__useraccount = useraccount

    @property
    def list(self) -> str:
        return self.__list

    @list.setter
    def list(self, list: str):
        self.__list = list

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

class dsl_ClickSendSms(Action):

    def __init__(self, value: str, userid: str, securityKey: str, target: str):
        self.value = value
        self.userid = userid
        self.securityKey = securityKey
        self.target = target
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def userid(self) -> str:
        return self.__userid

    @userid.setter
    def userid(self, userid: str):
        self.__userid = userid

    @property
    def securityKey(self) -> str:
        return self.__securityKey

    @securityKey.setter
    def securityKey(self, securityKey: str):
        self.__securityKey = securityKey

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class dsl_Copydata(Action):

    def __init__(self, source: str, to: str, value: str):
        self.source = source
        self.to = to
        self.value = value
        
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

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dsl_GooglecalPUT(Action):

    def __init__(self, account: str, privateKey: str, ptwelveFile: str, project: str, impersonatedUser: str, dbSrc: str, value: str):
        self.account = account
        self.privateKey = privateKey
        self.ptwelveFile = ptwelveFile
        self.project = project
        self.impersonatedUser = impersonatedUser
        self.dbSrc = dbSrc
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def dbSrc(self) -> str:
        return self.__dbSrc

    @dbSrc.setter
    def dbSrc(self, dbSrc: str):
        self.__dbSrc = dbSrc

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, account: str):
        self.__account = account

    @property
    def ptwelveFile(self) -> str:
        return self.__ptwelveFile

    @ptwelveFile.setter
    def ptwelveFile(self, ptwelveFile: str):
        self.__ptwelveFile = ptwelveFile

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

    @property
    def impersonatedUser(self) -> str:
        return self.__impersonatedUser

    @impersonatedUser.setter
    def impersonatedUser(self, impersonatedUser: str):
        self.__impersonatedUser = impersonatedUser

class dsl_Transform(Action):

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

class dsl_Doozle(Action):

    def __init__(self, target: str, on: str, value: str):
        self.target = target
        self.on = on
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

    @property
    def on(self) -> str:
        return self.__on

    @on.setter
    def on(self, on: str):
        self.__on = on

class dsl_FirebaseDatabasePut(Action):

    def __init__(self, url: str, fbjson: str, groupPath: str, dbSrc: str, classFqn: str, value: str):
        self.url = url
        self.fbjson = fbjson
        self.groupPath = groupPath
        self.dbSrc = dbSrc
        self.classFqn = classFqn
        self.value = value
        
    @property
    def dbSrc(self) -> str:
        return self.__dbSrc

    @dbSrc.setter
    def dbSrc(self, dbSrc: str):
        self.__dbSrc = dbSrc

    @property
    def groupPath(self) -> str:
        return self.__groupPath

    @groupPath.setter
    def groupPath(self, groupPath: str):
        self.__groupPath = groupPath

    @property
    def classFqn(self) -> str:
        return self.__classFqn

    @classFqn.setter
    def classFqn(self, classFqn: str):
        self.__classFqn = classFqn

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def fbjson(self) -> str:
        return self.__fbjson

    @fbjson.setter
    def fbjson(self, fbjson: str):
        self.__fbjson = fbjson

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dsl_Fetch(Action):

    def __init__(self, source: str, value: str):
        self.source = source
        self.value = value
        
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

class dsl_FirebaseReactiveNotification(Action):

    def __init__(self, url: str, fbjson: str, groupPath: str, classFqn: str, dbSrc: str):
        self.url = url
        self.fbjson = fbjson
        self.groupPath = groupPath
        self.classFqn = classFqn
        self.dbSrc = dbSrc
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def fbjson(self) -> str:
        return self.__fbjson

    @fbjson.setter
    def fbjson(self, fbjson: str):
        self.__fbjson = fbjson

    @property
    def classFqn(self) -> str:
        return self.__classFqn

    @classFqn.setter
    def classFqn(self, classFqn: str):
        self.__classFqn = classFqn

    @property
    def groupPath(self) -> str:
        return self.__groupPath

    @groupPath.setter
    def groupPath(self, groupPath: str):
        self.__groupPath = groupPath

    @property
    def dbSrc(self) -> str:
        return self.__dbSrc

    @dbSrc.setter
    def dbSrc(self, dbSrc: str):
        self.__dbSrc = dbSrc

class dsl_SlackPUT(Action):

    def __init__(self, team: str, channel: str, value: str):
        self.team = team
        self.channel = channel
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def team(self) -> str:
        return self.__team

    @team.setter
    def team(self, team: str):
        self.__team = team

    @property
    def channel(self) -> str:
        return self.__channel

    @channel.setter
    def channel(self, channel: str):
        self.__channel = channel

class dsl_Dropfile(Action):

    def __init__(self, target: str):
        self.target = target
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class dsl_GooglecontactSelectAll(Action):

    def __init__(self, account: str, privateKey: str, ptwelveFile: str, project: str, impersonatedUser: str, dbSrc: str, value: str):
        self.account = account
        self.privateKey = privateKey
        self.ptwelveFile = ptwelveFile
        self.project = project
        self.impersonatedUser = impersonatedUser
        self.dbSrc = dbSrc
        self.value = value
        
    @property
    def ptwelveFile(self) -> str:
        return self.__ptwelveFile

    @ptwelveFile.setter
    def ptwelveFile(self, ptwelveFile: str):
        self.__ptwelveFile = ptwelveFile

    @property
    def dbSrc(self) -> str:
        return self.__dbSrc

    @dbSrc.setter
    def dbSrc(self, dbSrc: str):
        self.__dbSrc = dbSrc

    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def impersonatedUser(self) -> str:
        return self.__impersonatedUser

    @impersonatedUser.setter
    def impersonatedUser(self, impersonatedUser: str):
        self.__impersonatedUser = impersonatedUser

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, account: str):
        self.__account = account

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

class dsl_SmsLeadSms(Action):

    def __init__(self, url: str, sender: str, account: str, privateKey: str, dbSrc: str, value: str, dryrunNumber: str):
        self.url = url
        self.sender = sender
        self.account = account
        self.privateKey = privateKey
        self.dbSrc = dbSrc
        self.value = value
        self.dryrunNumber = dryrunNumber
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def dbSrc(self) -> str:
        return self.__dbSrc

    @dbSrc.setter
    def dbSrc(self, dbSrc: str):
        self.__dbSrc = dbSrc

    @property
    def privateKey(self) -> str:
        return self.__privateKey

    @privateKey.setter
    def privateKey(self, privateKey: str):
        self.__privateKey = privateKey

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, account: str):
        self.__account = account

    @property
    def sender(self) -> str:
        return self.__sender

    @sender.setter
    def sender(self, sender: str):
        self.__sender = sender

    @property
    def dryrunNumber(self) -> str:
        return self.__dryrunNumber

    @dryrunNumber.setter
    def dryrunNumber(self, dryrunNumber: str):
        self.__dryrunNumber = dryrunNumber

class dsl_ExecJava(Action):

    def __init__(self, classFqn: str, dbSrc: str, value: str):
        self.classFqn = classFqn
        self.dbSrc = dbSrc
        self.value = value
        
    @property
    def dbSrc(self) -> str:
        return self.__dbSrc

    @dbSrc.setter
    def dbSrc(self, dbSrc: str):
        self.__dbSrc = dbSrc

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def classFqn(self) -> str:
        return self.__classFqn

    @classFqn.setter
    def classFqn(self, classFqn: str):
        self.__classFqn = classFqn

class dsl_Expression:

    def __init__(self, lhs: str, operator: str, rhs: str, dsl_Expression: "dsl_Action" = None):
        self.lhs = lhs
        self.operator = operator
        self.rhs = rhs
        self.dsl_Expression = dsl_Expression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

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
    def dsl_Expression(self):
        return self.__dsl_Expression

    @dsl_Expression.setter
    def dsl_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Expression__dsl_Expression", None)
        self.__dsl_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action14"):
                opp_val = getattr(old_value, "dsl_Action14", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action14"):
                opp_val = getattr(value, "dsl_Action14", None)
                setattr(value, "dsl_Action14", self)

class dsl_Action:

    def __init__(self, name: str, dsl_Action: "dsl_Try" = None, dsl_Action14: "dsl_Expression" = None, dsl_Action9: "dsl_Finally" = None, dsl_Action12: "dsl_Catch" = None):
        self.name = name
        self.dsl_Action = dsl_Action
        self.dsl_Action14 = dsl_Action14
        self.dsl_Action9 = dsl_Action9
        self.dsl_Action12 = dsl_Action12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Action(self):
        return self.__dsl_Action

    @dsl_Action.setter
    def dsl_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Action__dsl_Action", None)
        self.__dsl_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Try6"):
                opp_val = getattr(old_value, "dsl_Try6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Try6"):
                opp_val = getattr(value, "dsl_Try6", None)
                if opp_val is None:
                    setattr(value, "dsl_Try6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Action9(self):
        return self.__dsl_Action9

    @dsl_Action9.setter
    def dsl_Action9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Action__dsl_Action9", None)
        self.__dsl_Action9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Finally8"):
                opp_val = getattr(old_value, "dsl_Finally8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Finally8"):
                opp_val = getattr(value, "dsl_Finally8", None)
                if opp_val is None:
                    setattr(value, "dsl_Finally8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Action14(self):
        return self.__dsl_Action14

    @dsl_Action14.setter
    def dsl_Action14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Action__dsl_Action14", None)
        self.__dsl_Action14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Expression"):
                opp_val = getattr(old_value, "dsl_Expression", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Expression"):
                opp_val = getattr(value, "dsl_Expression", None)
                setattr(value, "dsl_Expression", self)

    @property
    def dsl_Action12(self):
        return self.__dsl_Action12

    @dsl_Action12.setter
    def dsl_Action12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Action__dsl_Action12", None)
        self.__dsl_Action12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Catch11"):
                opp_val = getattr(old_value, "dsl_Catch11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Catch11"):
                opp_val = getattr(value, "dsl_Catch11", None)
                if opp_val is None:
                    setattr(value, "dsl_Catch11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Finally:

    def __init__(self, name: str, dsl_Finally: "dsl_Process" = None, dsl_Finally8: set["dsl_Action"] = None):
        self.name = name
        self.dsl_Finally = dsl_Finally
        self.dsl_Finally8 = dsl_Finally8 if dsl_Finally8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Finally8(self):
        return self.__dsl_Finally8

    @dsl_Finally8.setter
    def dsl_Finally8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Finally__dsl_Finally8", None)
        self.__dsl_Finally8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Action9"):
                    opp_val = getattr(item, "dsl_Action9", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Action9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Action9"):
                    opp_val = getattr(item, "dsl_Action9", None)
                    
                    setattr(item, "dsl_Action9", self)
                    

    @property
    def dsl_Finally(self):
        return self.__dsl_Finally

    @dsl_Finally.setter
    def dsl_Finally(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Finally__dsl_Finally", None)
        self.__dsl_Finally = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Process4"):
                opp_val = getattr(old_value, "dsl_Process4", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Process4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Process4"):
                opp_val = getattr(value, "dsl_Process4", None)
                setattr(value, "dsl_Process4", self)

class dsl_Catch:

    def __init__(self, name: str, dsl_Catch: "dsl_Process" = None, dsl_Catch11: set["dsl_Action"] = None):
        self.name = name
        self.dsl_Catch = dsl_Catch
        self.dsl_Catch11 = dsl_Catch11 if dsl_Catch11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Catch(self):
        return self.__dsl_Catch

    @dsl_Catch.setter
    def dsl_Catch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Catch__dsl_Catch", None)
        self.__dsl_Catch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Process2"):
                opp_val = getattr(old_value, "dsl_Process2", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Process2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Process2"):
                opp_val = getattr(value, "dsl_Process2", None)
                setattr(value, "dsl_Process2", self)

    @property
    def dsl_Catch11(self):
        return self.__dsl_Catch11

    @dsl_Catch11.setter
    def dsl_Catch11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Catch__dsl_Catch11", None)
        self.__dsl_Catch11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Action12"):
                    opp_val = getattr(item, "dsl_Action12", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Action12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Action12"):
                    opp_val = getattr(item, "dsl_Action12", None)
                    
                    setattr(item, "dsl_Action12", self)
                    

class dsl_Try:

    def __init__(self, name: str, dsl_Try: "dsl_Process" = None, dsl_Try6: set["dsl_Action"] = None):
        self.name = name
        self.dsl_Try = dsl_Try
        self.dsl_Try6 = dsl_Try6 if dsl_Try6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Try6(self):
        return self.__dsl_Try6

    @dsl_Try6.setter
    def dsl_Try6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Try__dsl_Try6", None)
        self.__dsl_Try6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Action"):
                    opp_val = getattr(item, "dsl_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Action"):
                    opp_val = getattr(item, "dsl_Action", None)
                    
                    setattr(item, "dsl_Action", self)
                    

    @property
    def dsl_Try(self):
        return self.__dsl_Try

    @dsl_Try.setter
    def dsl_Try(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Try__dsl_Try", None)
        self.__dsl_Try = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Process"):
                opp_val = getattr(old_value, "dsl_Process", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Process", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Process"):
                opp_val = getattr(value, "dsl_Process", None)
                setattr(value, "dsl_Process", self)

class dsl_Process:

    def __init__(self, name: str, dsl_Process: "dsl_Try" = None, dsl_Process2: "dsl_Catch" = None, dsl_Process4: "dsl_Finally" = None):
        self.name = name
        self.dsl_Process = dsl_Process
        self.dsl_Process2 = dsl_Process2
        self.dsl_Process4 = dsl_Process4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Process4(self):
        return self.__dsl_Process4

    @dsl_Process4.setter
    def dsl_Process4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Process__dsl_Process4", None)
        self.__dsl_Process4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Finally"):
                opp_val = getattr(old_value, "dsl_Finally", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Finally", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Finally"):
                opp_val = getattr(value, "dsl_Finally", None)
                setattr(value, "dsl_Finally", self)

    @property
    def dsl_Process(self):
        return self.__dsl_Process

    @dsl_Process.setter
    def dsl_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Process__dsl_Process", None)
        self.__dsl_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Try"):
                opp_val = getattr(old_value, "dsl_Try", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Try", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Try"):
                opp_val = getattr(value, "dsl_Try", None)
                setattr(value, "dsl_Try", self)

    @property
    def dsl_Process2(self):
        return self.__dsl_Process2

    @dsl_Process2.setter
    def dsl_Process2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Process__dsl_Process2", None)
        self.__dsl_Process2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Catch"):
                opp_val = getattr(old_value, "dsl_Catch", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Catch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Catch"):
                opp_val = getattr(value, "dsl_Catch", None)
                setattr(value, "dsl_Catch", self)
