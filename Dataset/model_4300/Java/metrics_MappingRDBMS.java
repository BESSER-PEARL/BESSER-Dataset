





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRDBMS extends Mapping {

    private String dateTimeFormat;
    private String user;
    private String databaseType;
    private String timeFormat;
    private String password;
    private String query;
    private String dateFormat;



    public metrics_MappingRDBMS(
        String dateTimeFormat,        String user,        String databaseType,        String timeFormat,        String password,        String query,        String dateFormat    ) {
        super(
        );
        this.dateTimeFormat = dateTimeFormat;
        this.user = user;
        this.databaseType = databaseType;
        this.timeFormat = timeFormat;
        this.password = password;
        this.query = query;
        this.dateFormat = dateFormat;
    }


    public String getDatetimeformat() {
        return dateTimeFormat;
    }

    public void setDatetimeformat(String dateTimeFormat) {
        this.dateTimeFormat = dateTimeFormat;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getDatabasetype() {
        return databaseType;
    }

    public void setDatabasetype(String databaseType) {
        this.databaseType = databaseType;
    }
    public String getTimeformat() {
        return timeFormat;
    }

    public void setTimeformat(String timeFormat) {
        this.timeFormat = timeFormat;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }
    public String getDateformat() {
        return dateFormat;
    }

    public void setDateformat(String dateFormat) {
        this.dateFormat = dateFormat;
    }


}