





import java.util.List;
import java.util.ArrayList;

public class connection_DatabaseConnection extends Connection {

    private String StringQuote;
    private boolean SystemSQL;
    private String URL;
    private boolean SQLMode;
    private String dbVersionString;
    private String SID;
    private boolean StandardSQL;
    private String Password;
    private String Username;
    private String DatabaseType;
    private String AdditionalParams;
    private String ProductId;
    private String DatasourceName;
    private String ServerName;
    private String Schema;
    private String DbmsId;
    private String DriverClass;
    private String cdcTypeMode;
    private String Port;
    private String DriverJarPath;
    private String SqlSynthax;
    private String FileFieldName;
    private String DBRootPath;
    private String NullChar;



    public connection_DatabaseConnection(
        String StringQuote,        boolean SystemSQL,        String URL,        boolean SQLMode,        String dbVersionString,        String SID,        boolean StandardSQL,        String Password,        String Username,        String DatabaseType,        String AdditionalParams,        String ProductId,        String DatasourceName,        String ServerName,        String Schema,        String DbmsId,        String DriverClass,        String cdcTypeMode,        String Port,        String DriverJarPath,        String SqlSynthax,        String FileFieldName,        String DBRootPath,        String NullChar    ) {
        super(
        );
        this.StringQuote = StringQuote;
        this.SystemSQL = SystemSQL;
        this.URL = URL;
        this.SQLMode = SQLMode;
        this.dbVersionString = dbVersionString;
        this.SID = SID;
        this.StandardSQL = StandardSQL;
        this.Password = Password;
        this.Username = Username;
        this.DatabaseType = DatabaseType;
        this.AdditionalParams = AdditionalParams;
        this.ProductId = ProductId;
        this.DatasourceName = DatasourceName;
        this.ServerName = ServerName;
        this.Schema = Schema;
        this.DbmsId = DbmsId;
        this.DriverClass = DriverClass;
        this.cdcTypeMode = cdcTypeMode;
        this.Port = Port;
        this.DriverJarPath = DriverJarPath;
        this.SqlSynthax = SqlSynthax;
        this.FileFieldName = FileFieldName;
        this.DBRootPath = DBRootPath;
        this.NullChar = NullChar;
    }


    public String getStringquote() {
        return StringQuote;
    }

    public void setStringquote(String StringQuote) {
        this.StringQuote = StringQuote;
    }
    public boolean getSystemsql() {
        return SystemSQL;
    }

    public void setSystemsql(boolean SystemSQL) {
        this.SystemSQL = SystemSQL;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public boolean getSqlmode() {
        return SQLMode;
    }

    public void setSqlmode(boolean SQLMode) {
        this.SQLMode = SQLMode;
    }
    public String getDbversionstring() {
        return dbVersionString;
    }

    public void setDbversionstring(String dbVersionString) {
        this.dbVersionString = dbVersionString;
    }
    public String getSid() {
        return SID;
    }

    public void setSid(String SID) {
        this.SID = SID;
    }
    public boolean getStandardsql() {
        return StandardSQL;
    }

    public void setStandardsql(boolean StandardSQL) {
        this.StandardSQL = StandardSQL;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getDatabasetype() {
        return DatabaseType;
    }

    public void setDatabasetype(String DatabaseType) {
        this.DatabaseType = DatabaseType;
    }
    public String getAdditionalparams() {
        return AdditionalParams;
    }

    public void setAdditionalparams(String AdditionalParams) {
        this.AdditionalParams = AdditionalParams;
    }
    public String getProductid() {
        return ProductId;
    }

    public void setProductid(String ProductId) {
        this.ProductId = ProductId;
    }
    public String getDatasourcename() {
        return DatasourceName;
    }

    public void setDatasourcename(String DatasourceName) {
        this.DatasourceName = DatasourceName;
    }
    public String getServername() {
        return ServerName;
    }

    public void setServername(String ServerName) {
        this.ServerName = ServerName;
    }
    public String getSchema() {
        return Schema;
    }

    public void setSchema(String Schema) {
        this.Schema = Schema;
    }
    public String getDbmsid() {
        return DbmsId;
    }

    public void setDbmsid(String DbmsId) {
        this.DbmsId = DbmsId;
    }
    public String getDriverclass() {
        return DriverClass;
    }

    public void setDriverclass(String DriverClass) {
        this.DriverClass = DriverClass;
    }
    public String getCdctypemode() {
        return cdcTypeMode;
    }

    public void setCdctypemode(String cdcTypeMode) {
        this.cdcTypeMode = cdcTypeMode;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getDriverjarpath() {
        return DriverJarPath;
    }

    public void setDriverjarpath(String DriverJarPath) {
        this.DriverJarPath = DriverJarPath;
    }
    public String getSqlsynthax() {
        return SqlSynthax;
    }

    public void setSqlsynthax(String SqlSynthax) {
        this.SqlSynthax = SqlSynthax;
    }
    public String getFilefieldname() {
        return FileFieldName;
    }

    public void setFilefieldname(String FileFieldName) {
        this.FileFieldName = FileFieldName;
    }
    public String getDbrootpath() {
        return DBRootPath;
    }

    public void setDbrootpath(String DBRootPath) {
        this.DBRootPath = DBRootPath;
    }
    public String getNullchar() {
        return NullChar;
    }

    public void setNullchar(String NullChar) {
        this.NullChar = NullChar;
    }


}