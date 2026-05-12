





import java.util.List;
import java.util.ArrayList;

public class properties_DatabaseProperties  {

    private String password;
    private String serverURL;
    private String namespace;
    private String id;
    private String driverClassName;
    private String dBMS;
    private String username;
    private String dialect;
    private String persistenceUnitName;
    private String databaseName;
    private String port;



    public properties_DatabaseProperties(
        String password,        String serverURL,        String namespace,        String id,        String driverClassName,        String dBMS,        String username,        String dialect,        String persistenceUnitName,        String databaseName,        String port    ) {
        this.password = password;
        this.serverURL = serverURL;
        this.namespace = namespace;
        this.id = id;
        this.driverClassName = driverClassName;
        this.dBMS = dBMS;
        this.username = username;
        this.dialect = dialect;
        this.persistenceUnitName = persistenceUnitName;
        this.databaseName = databaseName;
        this.port = port;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getServerurl() {
        return serverURL;
    }

    public void setServerurl(String serverURL) {
        this.serverURL = serverURL;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDriverclassname() {
        return driverClassName;
    }

    public void setDriverclassname(String driverClassName) {
        this.driverClassName = driverClassName;
    }
    public String getDbms() {
        return dBMS;
    }

    public void setDbms(String dBMS) {
        this.dBMS = dBMS;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getDialect() {
        return dialect;
    }

    public void setDialect(String dialect) {
        this.dialect = dialect;
    }
    public String getPersistenceunitname() {
        return persistenceUnitName;
    }

    public void setPersistenceunitname(String persistenceUnitName) {
        this.persistenceUnitName = persistenceUnitName;
    }
    public String getDatabasename() {
        return databaseName;
    }

    public void setDatabasename(String databaseName) {
        this.databaseName = databaseName;
    }
    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }


}