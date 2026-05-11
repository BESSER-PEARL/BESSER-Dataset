





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRDBMS extends Mapping {

    private String dateTimeFormat;
    private String timeFormat;
    private String databaseType;
    private String dateFormat;
    private String password;
    private String query;
    private String user;



    public metrics_MappingRDBMS(
        String dateTimeFormat,        String timeFormat,        String databaseType,        String dateFormat,        String password,        String query,        String user    ) {
        super(
        );
        this.dateTimeFormat = dateTimeFormat;
        this.timeFormat = timeFormat;
        this.databaseType = databaseType;
        this.dateFormat = dateFormat;
        this.password = password;
        this.query = query;
        this.user = user;
    }


    public String getDatetimeformat() {
        return dateTimeFormat;
    }

    public void setDatetimeformat(String dateTimeFormat) {
        this.dateTimeFormat = dateTimeFormat;
    }
    public String getTimeformat() {
        return timeFormat;
    }

    public void setTimeformat(String timeFormat) {
        this.timeFormat = timeFormat;
    }
    public String getDatabasetype() {
        return databaseType;
    }

    public void setDatabasetype(String databaseType) {
        this.databaseType = databaseType;
    }
    public String getDateformat() {
        return dateFormat;
    }

    public void setDateformat(String dateFormat) {
        this.dateFormat = dateFormat;
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
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }


}