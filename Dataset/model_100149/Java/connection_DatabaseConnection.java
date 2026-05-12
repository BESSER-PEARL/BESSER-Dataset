





import java.util.List;
import java.util.ArrayList;

public class connection_DatabaseConnection extends Connection {

    private String AdditionalParams;
    private String FileFieldName;
    private String DriverJarPath;
    private String DatasourceName;
    private String dbVersionString;
    private boolean SQLMode;
    private String ProductId;
    private String DBRootPath;
    private String DriverClass;
    private String ServerName;
    private String URL;
    private String Port;
    private String SqlSynthax;
    private String DatabaseType;
    private String Password;
    private String DbmsId;
    private boolean StandardSQL;
    private boolean SystemSQL;
    private String SID;
    private String cdcTypeMode;
    private String NullChar;
    private String StringQuote;
    private String UiSchema;
    private String Username;





    private List<connection_AdditionalProperties> connection_additionalpropertiess;


    public connection_DatabaseConnection(
        String AdditionalParams,        String FileFieldName,        String DriverJarPath,        String DatasourceName,        String dbVersionString,        boolean SQLMode,        String ProductId,        String DBRootPath,        String DriverClass,        String ServerName,        String URL,        String Port,        String SqlSynthax,        String DatabaseType,        String Password,        String DbmsId,        boolean StandardSQL,        boolean SystemSQL,        String SID,        String cdcTypeMode,        String NullChar,        String StringQuote,        String UiSchema,        String Username    ) {
        super(
        );
        this.AdditionalParams = AdditionalParams;
        this.FileFieldName = FileFieldName;
        this.DriverJarPath = DriverJarPath;
        this.DatasourceName = DatasourceName;
        this.dbVersionString = dbVersionString;
        this.SQLMode = SQLMode;
        this.ProductId = ProductId;
        this.DBRootPath = DBRootPath;
        this.DriverClass = DriverClass;
        this.ServerName = ServerName;
        this.URL = URL;
        this.Port = Port;
        this.SqlSynthax = SqlSynthax;
        this.DatabaseType = DatabaseType;
        this.Password = Password;
        this.DbmsId = DbmsId;
        this.StandardSQL = StandardSQL;
        this.SystemSQL = SystemSQL;
        this.SID = SID;
        this.cdcTypeMode = cdcTypeMode;
        this.NullChar = NullChar;
        this.StringQuote = StringQuote;
        this.UiSchema = UiSchema;
        this.Username = Username;
        this.connection_additionalpropertiess = new ArrayList<>();
    }

    public connection_DatabaseConnection(
        String AdditionalParams,        String FileFieldName,        String DriverJarPath,        String DatasourceName,        String dbVersionString,        boolean SQLMode,        String ProductId,        String DBRootPath,        String DriverClass,        String ServerName,        String URL,        String Port,        String SqlSynthax,        String DatabaseType,        String Password,        String DbmsId,        boolean StandardSQL,        boolean SystemSQL,        String SID,        String cdcTypeMode,        String NullChar,        String StringQuote,        String UiSchema,        String Username        ArrayList<connection_AdditionalProperties> connection_additionalpropertiess    ) {
        this.AdditionalParams = AdditionalParams;
        this.FileFieldName = FileFieldName;
        this.DriverJarPath = DriverJarPath;
        this.DatasourceName = DatasourceName;
        this.dbVersionString = dbVersionString;
        this.SQLMode = SQLMode;
        this.ProductId = ProductId;
        this.DBRootPath = DBRootPath;
        this.DriverClass = DriverClass;
        this.ServerName = ServerName;
        this.URL = URL;
        this.Port = Port;
        this.SqlSynthax = SqlSynthax;
        this.DatabaseType = DatabaseType;
        this.Password = Password;
        this.DbmsId = DbmsId;
        this.StandardSQL = StandardSQL;
        this.SystemSQL = SystemSQL;
        this.SID = SID;
        this.cdcTypeMode = cdcTypeMode;
        this.NullChar = NullChar;
        this.StringQuote = StringQuote;
        this.UiSchema = UiSchema;
        this.Username = Username;
        this.connection_additionalpropertiess = connection_additionalpropertiess;
    }

    public String getAdditionalparams() {
        return AdditionalParams;
    }

    public void setAdditionalparams(String AdditionalParams) {
        this.AdditionalParams = AdditionalParams;
    }
    public String getFilefieldname() {
        return FileFieldName;
    }

    public void setFilefieldname(String FileFieldName) {
        this.FileFieldName = FileFieldName;
    }
    public String getDriverjarpath() {
        return DriverJarPath;
    }

    public void setDriverjarpath(String DriverJarPath) {
        this.DriverJarPath = DriverJarPath;
    }
    public String getDatasourcename() {
        return DatasourceName;
    }

    public void setDatasourcename(String DatasourceName) {
        this.DatasourceName = DatasourceName;
    }
    public String getDbversionstring() {
        return dbVersionString;
    }

    public void setDbversionstring(String dbVersionString) {
        this.dbVersionString = dbVersionString;
    }
    public boolean getSqlmode() {
        return SQLMode;
    }

    public void setSqlmode(boolean SQLMode) {
        this.SQLMode = SQLMode;
    }
    public String getProductid() {
        return ProductId;
    }

    public void setProductid(String ProductId) {
        this.ProductId = ProductId;
    }
    public String getDbrootpath() {
        return DBRootPath;
    }

    public void setDbrootpath(String DBRootPath) {
        this.DBRootPath = DBRootPath;
    }
    public String getDriverclass() {
        return DriverClass;
    }

    public void setDriverclass(String DriverClass) {
        this.DriverClass = DriverClass;
    }
    public String getServername() {
        return ServerName;
    }

    public void setServername(String ServerName) {
        this.ServerName = ServerName;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getSqlsynthax() {
        return SqlSynthax;
    }

    public void setSqlsynthax(String SqlSynthax) {
        this.SqlSynthax = SqlSynthax;
    }
    public String getDatabasetype() {
        return DatabaseType;
    }

    public void setDatabasetype(String DatabaseType) {
        this.DatabaseType = DatabaseType;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getDbmsid() {
        return DbmsId;
    }

    public void setDbmsid(String DbmsId) {
        this.DbmsId = DbmsId;
    }
    public boolean getStandardsql() {
        return StandardSQL;
    }

    public void setStandardsql(boolean StandardSQL) {
        this.StandardSQL = StandardSQL;
    }
    public boolean getSystemsql() {
        return SystemSQL;
    }

    public void setSystemsql(boolean SystemSQL) {
        this.SystemSQL = SystemSQL;
    }
    public String getSid() {
        return SID;
    }

    public void setSid(String SID) {
        this.SID = SID;
    }
    public String getCdctypemode() {
        return cdcTypeMode;
    }

    public void setCdctypemode(String cdcTypeMode) {
        this.cdcTypeMode = cdcTypeMode;
    }
    public String getNullchar() {
        return NullChar;
    }

    public void setNullchar(String NullChar) {
        this.NullChar = NullChar;
    }
    public String getStringquote() {
        return StringQuote;
    }

    public void setStringquote(String StringQuote) {
        this.StringQuote = StringQuote;
    }
    public String getUischema() {
        return UiSchema;
    }

    public void setUischema(String UiSchema) {
        this.UiSchema = UiSchema;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }

    public List<connection_AdditionalProperties> getConnection_additionalpropertiess() {
        return connection_additionalpropertiess;
    }

    public void addConnection_additionalproperties(Connection_additionalproperties connection_additionalproperties) {
        this.connection_additionalpropertiess.add(connection_additionalproperties);
    }

}