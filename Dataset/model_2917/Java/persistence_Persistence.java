





import java.util.List;
import java.util.ArrayList;

public class persistence_Persistence  {

    private String databasePrefix;
    private boolean timestampCreation;
    private String databaseHost;
    private String databasePort;
    private String databaseName;
    private String databaseTechnology;
    private boolean timestampUpdates;
    private String ormTechnology;
    private String databasePassword;
    private String databaseUsername;



    public persistence_Persistence(
        String databasePrefix,        boolean timestampCreation,        String databaseHost,        String databasePort,        String databaseName,        String databaseTechnology,        boolean timestampUpdates,        String ormTechnology,        String databasePassword,        String databaseUsername    ) {
        this.databasePrefix = databasePrefix;
        this.timestampCreation = timestampCreation;
        this.databaseHost = databaseHost;
        this.databasePort = databasePort;
        this.databaseName = databaseName;
        this.databaseTechnology = databaseTechnology;
        this.timestampUpdates = timestampUpdates;
        this.ormTechnology = ormTechnology;
        this.databasePassword = databasePassword;
        this.databaseUsername = databaseUsername;
    }


    public String getDatabaseprefix() {
        return databasePrefix;
    }

    public void setDatabaseprefix(String databasePrefix) {
        this.databasePrefix = databasePrefix;
    }
    public boolean getTimestampcreation() {
        return timestampCreation;
    }

    public void setTimestampcreation(boolean timestampCreation) {
        this.timestampCreation = timestampCreation;
    }
    public String getDatabasehost() {
        return databaseHost;
    }

    public void setDatabasehost(String databaseHost) {
        this.databaseHost = databaseHost;
    }
    public String getDatabaseport() {
        return databasePort;
    }

    public void setDatabaseport(String databasePort) {
        this.databasePort = databasePort;
    }
    public String getDatabasename() {
        return databaseName;
    }

    public void setDatabasename(String databaseName) {
        this.databaseName = databaseName;
    }
    public String getDatabasetechnology() {
        return databaseTechnology;
    }

    public void setDatabasetechnology(String databaseTechnology) {
        this.databaseTechnology = databaseTechnology;
    }
    public boolean getTimestampupdates() {
        return timestampUpdates;
    }

    public void setTimestampupdates(boolean timestampUpdates) {
        this.timestampUpdates = timestampUpdates;
    }
    public String getOrmtechnology() {
        return ormTechnology;
    }

    public void setOrmtechnology(String ormTechnology) {
        this.ormTechnology = ormTechnology;
    }
    public String getDatabasepassword() {
        return databasePassword;
    }

    public void setDatabasepassword(String databasePassword) {
        this.databasePassword = databasePassword;
    }
    public String getDatabaseusername() {
        return databaseUsername;
    }

    public void setDatabaseusername(String databaseUsername) {
        this.databaseUsername = databaseUsername;
    }


}