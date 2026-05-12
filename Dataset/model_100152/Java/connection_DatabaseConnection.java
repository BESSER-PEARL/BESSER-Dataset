





import java.util.List;
import java.util.ArrayList;

public class connection_DatabaseConnection extends Connection {

    private String DatasourceName;
    private boolean SystemSQL;
    private String ProductId;
    private String NullChar;
    private String DatabaseType;
    private String UiSchema;
    private String DBRootPath;
    private String DriverJarPath;
    private String Username;
    private String FileFieldName;
    private String DbmsId;
    private String Port;
    private String URL;
    private String DriverClass;
    private String AdditionalParams;
    private String cdcTypeMode;
    private String dbVersionString;
    private String StringQuote;
    private String SqlSynthax;
    private boolean SQLMode;
    private String ServerName;
    private String SID;
    private String Password;
    private boolean StandardSQL;



    public connection_DatabaseConnection(
        String DatasourceName,        boolean SystemSQL,        String ProductId,        String NullChar,        String DatabaseType,        String UiSchema,        String DBRootPath,        String DriverJarPath,        String Username,        String FileFieldName,        String DbmsId,        String Port,        String URL,        String DriverClass,        String AdditionalParams,        String cdcTypeMode,        String dbVersionString,        String StringQuote,        String SqlSynthax,        boolean SQLMode,        String ServerName,        String SID,        String Password,        boolean StandardSQL    ) {
        super(
        );
        this.DatasourceName = DatasourceName;
        this.SystemSQL = SystemSQL;
        this.ProductId = ProductId;
        this.NullChar = NullChar;
        this.DatabaseType = DatabaseType;
        this.UiSchema = UiSchema;
        this.DBRootPath = DBRootPath;
        this.DriverJarPath = DriverJarPath;
        this.Username = Username;
        this.FileFieldName = FileFieldName;
        this.DbmsId = DbmsId;
        this.Port = Port;
        this.URL = URL;
        this.DriverClass = DriverClass;
        this.AdditionalParams = AdditionalParams;
        this.cdcTypeMode = cdcTypeMode;
        this.dbVersionString = dbVersionString;
        this.StringQuote = StringQuote;
        this.SqlSynthax = SqlSynthax;
        this.SQLMode = SQLMode;
        this.ServerName = ServerName;
        this.SID = SID;
        this.Password = Password;
        this.StandardSQL = StandardSQL;
    }


    public String getDatasourcename() {
        return DatasourceName;
    }

    public void setDatasourcename(String DatasourceName) {
        this.DatasourceName = DatasourceName;
    }
    public boolean getSystemsql() {
        return SystemSQL;
    }

    public void setSystemsql(boolean SystemSQL) {
        this.SystemSQL = SystemSQL;
    }
    public String getProductid() {
        return ProductId;
    }

    public void setProductid(String ProductId) {
        this.ProductId = ProductId;
    }
    public String getNullchar() {
        return NullChar;
    }

    public void setNullchar(String NullChar) {
        this.NullChar = NullChar;
    }
    public String getDatabasetype() {
        return DatabaseType;
    }

    public void setDatabasetype(String DatabaseType) {
        this.DatabaseType = DatabaseType;
    }
    public String getUischema() {
        return UiSchema;
    }

    public void setUischema(String UiSchema) {
        this.UiSchema = UiSchema;
    }
    public String getDbrootpath() {
        return DBRootPath;
    }

    public void setDbrootpath(String DBRootPath) {
        this.DBRootPath = DBRootPath;
    }
    public String getDriverjarpath() {
        return DriverJarPath;
    }

    public void setDriverjarpath(String DriverJarPath) {
        this.DriverJarPath = DriverJarPath;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getFilefieldname() {
        return FileFieldName;
    }

    public void setFilefieldname(String FileFieldName) {
        this.FileFieldName = FileFieldName;
    }
    public String getDbmsid() {
        return DbmsId;
    }

    public void setDbmsid(String DbmsId) {
        this.DbmsId = DbmsId;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getDriverclass() {
        return DriverClass;
    }

    public void setDriverclass(String DriverClass) {
        this.DriverClass = DriverClass;
    }
    public String getAdditionalparams() {
        return AdditionalParams;
    }

    public void setAdditionalparams(String AdditionalParams) {
        this.AdditionalParams = AdditionalParams;
    }
    public String getCdctypemode() {
        return cdcTypeMode;
    }

    public void setCdctypemode(String cdcTypeMode) {
        this.cdcTypeMode = cdcTypeMode;
    }
    public String getDbversionstring() {
        return dbVersionString;
    }

    public void setDbversionstring(String dbVersionString) {
        this.dbVersionString = dbVersionString;
    }
    public String getStringquote() {
        return StringQuote;
    }

    public void setStringquote(String StringQuote) {
        this.StringQuote = StringQuote;
    }
    public String getSqlsynthax() {
        return SqlSynthax;
    }

    public void setSqlsynthax(String SqlSynthax) {
        this.SqlSynthax = SqlSynthax;
    }
    public boolean getSqlmode() {
        return SQLMode;
    }

    public void setSqlmode(boolean SQLMode) {
        this.SQLMode = SQLMode;
    }
    public String getServername() {
        return ServerName;
    }

    public void setServername(String ServerName) {
        this.ServerName = ServerName;
    }
    public String getSid() {
        return SID;
    }

    public void setSid(String SID) {
        this.SID = SID;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public boolean getStandardsql() {
        return StandardSQL;
    }

    public void setStandardsql(boolean StandardSQL) {
        this.StandardSQL = StandardSQL;
    }


}