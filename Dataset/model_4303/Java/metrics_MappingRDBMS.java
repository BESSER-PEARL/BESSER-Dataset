





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRDBMS extends Mapping {

    private String timeFormat;
    private String user;
    private String databaseType;
    private String dateTimeFormat;
    private String password;
    private String dateFormat;
    private String query;



    public metrics_MappingRDBMS(
        String timeFormat,        String user,        String databaseType,        String dateTimeFormat,        String password,        String dateFormat,        String query    ) {
        super(
        );
        this.timeFormat = timeFormat;
        this.user = user;
        this.databaseType = databaseType;
        this.dateTimeFormat = dateTimeFormat;
        this.password = password;
        this.dateFormat = dateFormat;
        this.query = query;
    }


    public String getTimeformat() {
        return timeFormat;
    }

    public void setTimeformat(String timeFormat) {
        this.timeFormat = timeFormat;
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
    public String getDatetimeformat() {
        return dateTimeFormat;
    }

    public void setDatetimeformat(String dateTimeFormat) {
        this.dateTimeFormat = dateTimeFormat;
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
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }


}