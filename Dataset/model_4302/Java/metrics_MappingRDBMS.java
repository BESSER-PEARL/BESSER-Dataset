





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRDBMS extends Mapping {

    private String user;
    private String password;
    private String dateFormat;
    private String timeFormat;
    private String dateTimeFormat;
    private String databaseType;
    private String query;



    public metrics_MappingRDBMS(
        String user,        String password,        String dateFormat,        String timeFormat,        String dateTimeFormat,        String databaseType,        String query    ) {
        super(
        );
        this.user = user;
        this.password = password;
        this.dateFormat = dateFormat;
        this.timeFormat = timeFormat;
        this.dateTimeFormat = dateTimeFormat;
        this.databaseType = databaseType;
        this.query = query;
    }


    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getDateformat() {
        return dateFormat;
    }

    public void setDateformat(String dateFormat) {
        this.dateFormat = dateFormat;
    }
    public String getTimeformat() {
        return timeFormat;
    }

    public void setTimeformat(String timeFormat) {
        this.timeFormat = timeFormat;
    }
    public String getDatetimeformat() {
        return dateTimeFormat;
    }

    public void setDatetimeformat(String dateTimeFormat) {
        this.dateTimeFormat = dateTimeFormat;
    }
    public String getDatabasetype() {
        return databaseType;
    }

    public void setDatabasetype(String databaseType) {
        this.databaseType = databaseType;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }


}