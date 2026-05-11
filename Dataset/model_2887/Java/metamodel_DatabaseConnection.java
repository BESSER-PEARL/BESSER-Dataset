





import java.util.List;
import java.util.ArrayList;

public class metamodel_DatabaseConnection  {

    private String jdbcPassword;
    private String jdbcDriver;
    private String jdbcUser;
    private String jdbcPrefix;
    private String jdbcUrl;
    private String persistenceUnit;



    public metamodel_DatabaseConnection(
        String jdbcPassword,        String jdbcDriver,        String jdbcUser,        String jdbcPrefix,        String jdbcUrl,        String persistenceUnit    ) {
        this.jdbcPassword = jdbcPassword;
        this.jdbcDriver = jdbcDriver;
        this.jdbcUser = jdbcUser;
        this.jdbcPrefix = jdbcPrefix;
        this.jdbcUrl = jdbcUrl;
        this.persistenceUnit = persistenceUnit;
    }


    public String getJdbcpassword() {
        return jdbcPassword;
    }

    public void setJdbcpassword(String jdbcPassword) {
        this.jdbcPassword = jdbcPassword;
    }
    public String getJdbcdriver() {
        return jdbcDriver;
    }

    public void setJdbcdriver(String jdbcDriver) {
        this.jdbcDriver = jdbcDriver;
    }
    public String getJdbcuser() {
        return jdbcUser;
    }

    public void setJdbcuser(String jdbcUser) {
        this.jdbcUser = jdbcUser;
    }
    public String getJdbcprefix() {
        return jdbcPrefix;
    }

    public void setJdbcprefix(String jdbcPrefix) {
        this.jdbcPrefix = jdbcPrefix;
    }
    public String getJdbcurl() {
        return jdbcUrl;
    }

    public void setJdbcurl(String jdbcUrl) {
        this.jdbcUrl = jdbcUrl;
    }
    public String getPersistenceunit() {
        return persistenceUnit;
    }

    public void setPersistenceunit(String persistenceUnit) {
        this.persistenceUnit = persistenceUnit;
    }


}