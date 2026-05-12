





import java.util.List;
import java.util.ArrayList;

public class connection_DatabaseConnection extends Connection {

    private String dbVersionString;
    private boolean SystemSQL;
    private String StringQuote;
    private boolean SQLMode;
    private String Password;
    private String UiSchema;
    private String Username;
    private boolean StandardSQL;
    private String DatasourceName;
    private String ProductId;
    private String FileFieldName;
    private String SqlSynthax;
    private String ServerName;
    private String NullChar;
    private String DriverClass;
    private String URL;
    private String cdcTypeMode;
    private String DatabaseType;
    private String DBRootPath;
    private String SID;
    private String AdditionalParams;
    private String DriverJarPath;
    private String Port;
    private String DbmsId;



    public connection_DatabaseConnection(
        String dbVersionString,        boolean SystemSQL,        String StringQuote,        boolean SQLMode,        String Password,        String UiSchema,        String Username,        boolean StandardSQL,        String DatasourceName,        String ProductId,        String FileFieldName,        String SqlSynthax,        String ServerName,        String NullChar,        String DriverClass,        String URL,        String cdcTypeMode,        String DatabaseType,        String DBRootPath,        String SID,        String AdditionalParams,        String DriverJarPath,        String Port,        String DbmsId    ) {
        super(
        );
        this.dbVersionString = dbVersionString;
        this.SystemSQL = SystemSQL;
        this.StringQuote = StringQuote;
        this.SQLMode = SQLMode;
        this.Password = Password;
        this.UiSchema = UiSchema;
        this.Username = Username;
        this.StandardSQL = StandardSQL;
        this.DatasourceName = DatasourceName;
        this.ProductId = ProductId;
        this.FileFieldName = FileFieldName;
        this.SqlSynthax = SqlSynthax;
        this.ServerName = ServerName;
        this.NullChar = NullChar;
        this.DriverClass = DriverClass;
        this.URL = URL;
        this.cdcTypeMode = cdcTypeMode;
        this.DatabaseType = DatabaseType;
        this.DBRootPath = DBRootPath;
        this.SID = SID;
        this.AdditionalParams = AdditionalParams;
        this.DriverJarPath = DriverJarPath;
        this.Port = Port;
        this.DbmsId = DbmsId;
    }


    public String getDbversionstring() {
        return dbVersionString;
    }

    public void setDbversionstring(String dbVersionString) {
        this.dbVersionString = dbVersionString;
    }
    public boolean getSystemsql() {
        return SystemSQL;
    }

    public void setSystemsql(boolean SystemSQL) {
        this.SystemSQL = SystemSQL;
    }
    public String getStringquote() {
        return StringQuote;
    }

    public void setStringquote(String StringQuote) {
        this.StringQuote = StringQuote;
    }
    public boolean getSqlmode() {
        return SQLMode;
    }

    public void setSqlmode(boolean SQLMode) {
        this.SQLMode = SQLMode;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
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
    public boolean getStandardsql() {
        return StandardSQL;
    }

    public void setStandardsql(boolean StandardSQL) {
        this.StandardSQL = StandardSQL;
    }
    public String getDatasourcename() {
        return DatasourceName;
    }

    public void setDatasourcename(String DatasourceName) {
        this.DatasourceName = DatasourceName;
    }
    public String getProductid() {
        return ProductId;
    }

    public void setProductid(String ProductId) {
        this.ProductId = ProductId;
    }
    public String getFilefieldname() {
        return FileFieldName;
    }

    public void setFilefieldname(String FileFieldName) {
        this.FileFieldName = FileFieldName;
    }
    public String getSqlsynthax() {
        return SqlSynthax;
    }

    public void setSqlsynthax(String SqlSynthax) {
        this.SqlSynthax = SqlSynthax;
    }
    public String getServername() {
        return ServerName;
    }

    public void setServername(String ServerName) {
        this.ServerName = ServerName;
    }
    public String getNullchar() {
        return NullChar;
    }

    public void setNullchar(String NullChar) {
        this.NullChar = NullChar;
    }
    public String getDriverclass() {
        return DriverClass;
    }

    public void setDriverclass(String DriverClass) {
        this.DriverClass = DriverClass;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getCdctypemode() {
        return cdcTypeMode;
    }

    public void setCdctypemode(String cdcTypeMode) {
        this.cdcTypeMode = cdcTypeMode;
    }
    public String getDatabasetype() {
        return DatabaseType;
    }

    public void setDatabasetype(String DatabaseType) {
        this.DatabaseType = DatabaseType;
    }
    public String getDbrootpath() {
        return DBRootPath;
    }

    public void setDbrootpath(String DBRootPath) {
        this.DBRootPath = DBRootPath;
    }
    public String getSid() {
        return SID;
    }

    public void setSid(String SID) {
        this.SID = SID;
    }
    public String getAdditionalparams() {
        return AdditionalParams;
    }

    public void setAdditionalparams(String AdditionalParams) {
        this.AdditionalParams = AdditionalParams;
    }
    public String getDriverjarpath() {
        return DriverJarPath;
    }

    public void setDriverjarpath(String DriverJarPath) {
        this.DriverJarPath = DriverJarPath;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getDbmsid() {
        return DbmsId;
    }

    public void setDbmsid(String DbmsId) {
        this.DbmsId = DbmsId;
    }


}