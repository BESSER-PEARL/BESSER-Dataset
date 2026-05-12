





import java.util.List;
import java.util.ArrayList;

public class connection_DatabaseConnection extends Connection {

    private String Password;
    private String Port;
    private String SqlSynthax;
    private String DbmsId;
    private String AdditionalParams;
    private String cdcTypeMode;
    private String DBRootPath;
    private String SID;
    private String dbVersionString;
    private boolean SystemSQL;
    private String DriverClass;
    private String NullChar;
    private String Username;
    private String DriverJarPath;
    private String URL;
    private String ServerName;
    private String StringQuote;
    private String ProductId;
    private String UiSchema;
    private String FileFieldName;
    private boolean StandardSQL;
    private String DatabaseType;
    private String DatasourceName;
    private boolean SQLMode;



    public connection_DatabaseConnection(
        String Password,        String Port,        String SqlSynthax,        String DbmsId,        String AdditionalParams,        String cdcTypeMode,        String DBRootPath,        String SID,        String dbVersionString,        boolean SystemSQL,        String DriverClass,        String NullChar,        String Username,        String DriverJarPath,        String URL,        String ServerName,        String StringQuote,        String ProductId,        String UiSchema,        String FileFieldName,        boolean StandardSQL,        String DatabaseType,        String DatasourceName,        boolean SQLMode    ) {
        super(
        );
        this.Password = Password;
        this.Port = Port;
        this.SqlSynthax = SqlSynthax;
        this.DbmsId = DbmsId;
        this.AdditionalParams = AdditionalParams;
        this.cdcTypeMode = cdcTypeMode;
        this.DBRootPath = DBRootPath;
        this.SID = SID;
        this.dbVersionString = dbVersionString;
        this.SystemSQL = SystemSQL;
        this.DriverClass = DriverClass;
        this.NullChar = NullChar;
        this.Username = Username;
        this.DriverJarPath = DriverJarPath;
        this.URL = URL;
        this.ServerName = ServerName;
        this.StringQuote = StringQuote;
        this.ProductId = ProductId;
        this.UiSchema = UiSchema;
        this.FileFieldName = FileFieldName;
        this.StandardSQL = StandardSQL;
        this.DatabaseType = DatabaseType;
        this.DatasourceName = DatasourceName;
        this.SQLMode = SQLMode;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
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
    public String getDbmsid() {
        return DbmsId;
    }

    public void setDbmsid(String DbmsId) {
        this.DbmsId = DbmsId;
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
    public String getDriverclass() {
        return DriverClass;
    }

    public void setDriverclass(String DriverClass) {
        this.DriverClass = DriverClass;
    }
    public String getNullchar() {
        return NullChar;
    }

    public void setNullchar(String NullChar) {
        this.NullChar = NullChar;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getDriverjarpath() {
        return DriverJarPath;
    }

    public void setDriverjarpath(String DriverJarPath) {
        this.DriverJarPath = DriverJarPath;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getServername() {
        return ServerName;
    }

    public void setServername(String ServerName) {
        this.ServerName = ServerName;
    }
    public String getStringquote() {
        return StringQuote;
    }

    public void setStringquote(String StringQuote) {
        this.StringQuote = StringQuote;
    }
    public String getProductid() {
        return ProductId;
    }

    public void setProductid(String ProductId) {
        this.ProductId = ProductId;
    }
    public String getUischema() {
        return UiSchema;
    }

    public void setUischema(String UiSchema) {
        this.UiSchema = UiSchema;
    }
    public String getFilefieldname() {
        return FileFieldName;
    }

    public void setFilefieldname(String FileFieldName) {
        this.FileFieldName = FileFieldName;
    }
    public boolean getStandardsql() {
        return StandardSQL;
    }

    public void setStandardsql(boolean StandardSQL) {
        this.StandardSQL = StandardSQL;
    }
    public String getDatabasetype() {
        return DatabaseType;
    }

    public void setDatabasetype(String DatabaseType) {
        this.DatabaseType = DatabaseType;
    }
    public String getDatasourcename() {
        return DatasourceName;
    }

    public void setDatasourcename(String DatasourceName) {
        this.DatasourceName = DatasourceName;
    }
    public boolean getSqlmode() {
        return SQLMode;
    }

    public void setSqlmode(boolean SQLMode) {
        this.SQLMode = SQLMode;
    }


}