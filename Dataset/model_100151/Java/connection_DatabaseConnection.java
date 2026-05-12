





import java.util.List;
import java.util.ArrayList;

public class connection_DatabaseConnection extends Connection {

    private String dbVersionString;
    private String Username;
    private String ProductId;
    private String SqlSynthax;
    private String Password;
    private String FileFieldName;
    private String AdditionalParams;
    private String DriverClass;
    private boolean SQLMode;
    private boolean SystemSQL;
    private String cdcTypeMode;
    private String StringQuote;
    private String URL;
    private String DriverJarPath;
    private String DbmsId;
    private String DatabaseType;
    private String Schema;
    private String ServerName;
    private String SID;
    private String Port;
    private boolean StandardSQL;
    private String DBRootPath;
    private String DatasourceName;
    private String NullChar;



    public connection_DatabaseConnection(
        String dbVersionString,        String Username,        String ProductId,        String SqlSynthax,        String Password,        String FileFieldName,        String AdditionalParams,        String DriverClass,        boolean SQLMode,        boolean SystemSQL,        String cdcTypeMode,        String StringQuote,        String URL,        String DriverJarPath,        String DbmsId,        String DatabaseType,        String Schema,        String ServerName,        String SID,        String Port,        boolean StandardSQL,        String DBRootPath,        String DatasourceName,        String NullChar    ) {
        super(
        );
        this.dbVersionString = dbVersionString;
        this.Username = Username;
        this.ProductId = ProductId;
        this.SqlSynthax = SqlSynthax;
        this.Password = Password;
        this.FileFieldName = FileFieldName;
        this.AdditionalParams = AdditionalParams;
        this.DriverClass = DriverClass;
        this.SQLMode = SQLMode;
        this.SystemSQL = SystemSQL;
        this.cdcTypeMode = cdcTypeMode;
        this.StringQuote = StringQuote;
        this.URL = URL;
        this.DriverJarPath = DriverJarPath;
        this.DbmsId = DbmsId;
        this.DatabaseType = DatabaseType;
        this.Schema = Schema;
        this.ServerName = ServerName;
        this.SID = SID;
        this.Port = Port;
        this.StandardSQL = StandardSQL;
        this.DBRootPath = DBRootPath;
        this.DatasourceName = DatasourceName;
        this.NullChar = NullChar;
    }


    public String getDbversionstring() {
        return dbVersionString;
    }

    public void setDbversionstring(String dbVersionString) {
        this.dbVersionString = dbVersionString;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getProductid() {
        return ProductId;
    }

    public void setProductid(String ProductId) {
        this.ProductId = ProductId;
    }
    public String getSqlsynthax() {
        return SqlSynthax;
    }

    public void setSqlsynthax(String SqlSynthax) {
        this.SqlSynthax = SqlSynthax;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getFilefieldname() {
        return FileFieldName;
    }

    public void setFilefieldname(String FileFieldName) {
        this.FileFieldName = FileFieldName;
    }
    public String getAdditionalparams() {
        return AdditionalParams;
    }

    public void setAdditionalparams(String AdditionalParams) {
        this.AdditionalParams = AdditionalParams;
    }
    public String getDriverclass() {
        return DriverClass;
    }

    public void setDriverclass(String DriverClass) {
        this.DriverClass = DriverClass;
    }
    public boolean getSqlmode() {
        return SQLMode;
    }

    public void setSqlmode(boolean SQLMode) {
        this.SQLMode = SQLMode;
    }
    public boolean getSystemsql() {
        return SystemSQL;
    }

    public void setSystemsql(boolean SystemSQL) {
        this.SystemSQL = SystemSQL;
    }
    public String getCdctypemode() {
        return cdcTypeMode;
    }

    public void setCdctypemode(String cdcTypeMode) {
        this.cdcTypeMode = cdcTypeMode;
    }
    public String getStringquote() {
        return StringQuote;
    }

    public void setStringquote(String StringQuote) {
        this.StringQuote = StringQuote;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getDriverjarpath() {
        return DriverJarPath;
    }

    public void setDriverjarpath(String DriverJarPath) {
        this.DriverJarPath = DriverJarPath;
    }
    public String getDbmsid() {
        return DbmsId;
    }

    public void setDbmsid(String DbmsId) {
        this.DbmsId = DbmsId;
    }
    public String getDatabasetype() {
        return DatabaseType;
    }

    public void setDatabasetype(String DatabaseType) {
        this.DatabaseType = DatabaseType;
    }
    public String getSchema() {
        return Schema;
    }

    public void setSchema(String Schema) {
        this.Schema = Schema;
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
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public boolean getStandardsql() {
        return StandardSQL;
    }

    public void setStandardsql(boolean StandardSQL) {
        this.StandardSQL = StandardSQL;
    }
    public String getDbrootpath() {
        return DBRootPath;
    }

    public void setDbrootpath(String DBRootPath) {
        this.DBRootPath = DBRootPath;
    }
    public String getDatasourcename() {
        return DatasourceName;
    }

    public void setDatasourcename(String DatasourceName) {
        this.DatasourceName = DatasourceName;
    }
    public String getNullchar() {
        return NullChar;
    }

    public void setNullchar(String NullChar) {
        this.NullChar = NullChar;
    }


}