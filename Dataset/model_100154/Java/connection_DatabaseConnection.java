





import java.util.List;
import java.util.ArrayList;

public class connection_DatabaseConnection extends Connection {

    private String Port;
    private String ServerName;
    private String UiSchema;
    private String DatabaseType;
    private String DriverJarPath;
    private String cdcTypeMode;
    private String AdditionalParams;
    private String Username;
    private String dbVersionString;
    private String FileFieldName;
    private String URL;
    private String DBRootPath;
    private String ProductId;
    private String Password;
    private String SqlSynthax;
    private boolean StandardSQL;
    private String DriverClass;
    private String DbmsId;
    private boolean SystemSQL;
    private String StringQuote;
    private String NullChar;
    private boolean SQLMode;
    private String DatasourceName;
    private String SID;



    public connection_DatabaseConnection(
        String Port,        String ServerName,        String UiSchema,        String DatabaseType,        String DriverJarPath,        String cdcTypeMode,        String AdditionalParams,        String Username,        String dbVersionString,        String FileFieldName,        String URL,        String DBRootPath,        String ProductId,        String Password,        String SqlSynthax,        boolean StandardSQL,        String DriverClass,        String DbmsId,        boolean SystemSQL,        String StringQuote,        String NullChar,        boolean SQLMode,        String DatasourceName,        String SID    ) {
        super(
        );
        this.Port = Port;
        this.ServerName = ServerName;
        this.UiSchema = UiSchema;
        this.DatabaseType = DatabaseType;
        this.DriverJarPath = DriverJarPath;
        this.cdcTypeMode = cdcTypeMode;
        this.AdditionalParams = AdditionalParams;
        this.Username = Username;
        this.dbVersionString = dbVersionString;
        this.FileFieldName = FileFieldName;
        this.URL = URL;
        this.DBRootPath = DBRootPath;
        this.ProductId = ProductId;
        this.Password = Password;
        this.SqlSynthax = SqlSynthax;
        this.StandardSQL = StandardSQL;
        this.DriverClass = DriverClass;
        this.DbmsId = DbmsId;
        this.SystemSQL = SystemSQL;
        this.StringQuote = StringQuote;
        this.NullChar = NullChar;
        this.SQLMode = SQLMode;
        this.DatasourceName = DatasourceName;
        this.SID = SID;
    }


    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getServername() {
        return ServerName;
    }

    public void setServername(String ServerName) {
        this.ServerName = ServerName;
    }
    public String getUischema() {
        return UiSchema;
    }

    public void setUischema(String UiSchema) {
        this.UiSchema = UiSchema;
    }
    public String getDatabasetype() {
        return DatabaseType;
    }

    public void setDatabasetype(String DatabaseType) {
        this.DatabaseType = DatabaseType;
    }
    public String getDriverjarpath() {
        return DriverJarPath;
    }

    public void setDriverjarpath(String DriverJarPath) {
        this.DriverJarPath = DriverJarPath;
    }
    public String getCdctypemode() {
        return cdcTypeMode;
    }

    public void setCdctypemode(String cdcTypeMode) {
        this.cdcTypeMode = cdcTypeMode;
    }
    public String getAdditionalparams() {
        return AdditionalParams;
    }

    public void setAdditionalparams(String AdditionalParams) {
        this.AdditionalParams = AdditionalParams;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getDbversionstring() {
        return dbVersionString;
    }

    public void setDbversionstring(String dbVersionString) {
        this.dbVersionString = dbVersionString;
    }
    public String getFilefieldname() {
        return FileFieldName;
    }

    public void setFilefieldname(String FileFieldName) {
        this.FileFieldName = FileFieldName;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getDbrootpath() {
        return DBRootPath;
    }

    public void setDbrootpath(String DBRootPath) {
        this.DBRootPath = DBRootPath;
    }
    public String getProductid() {
        return ProductId;
    }

    public void setProductid(String ProductId) {
        this.ProductId = ProductId;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getSqlsynthax() {
        return SqlSynthax;
    }

    public void setSqlsynthax(String SqlSynthax) {
        this.SqlSynthax = SqlSynthax;
    }
    public boolean getStandardsql() {
        return StandardSQL;
    }

    public void setStandardsql(boolean StandardSQL) {
        this.StandardSQL = StandardSQL;
    }
    public String getDriverclass() {
        return DriverClass;
    }

    public void setDriverclass(String DriverClass) {
        this.DriverClass = DriverClass;
    }
    public String getDbmsid() {
        return DbmsId;
    }

    public void setDbmsid(String DbmsId) {
        this.DbmsId = DbmsId;
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
    public String getNullchar() {
        return NullChar;
    }

    public void setNullchar(String NullChar) {
        this.NullChar = NullChar;
    }
    public boolean getSqlmode() {
        return SQLMode;
    }

    public void setSqlmode(boolean SQLMode) {
        this.SQLMode = SQLMode;
    }
    public String getDatasourcename() {
        return DatasourceName;
    }

    public void setDatasourcename(String DatasourceName) {
        this.DatasourceName = DatasourceName;
    }
    public String getSid() {
        return SID;
    }

    public void setSid(String SID) {
        this.SID = SID;
    }


}