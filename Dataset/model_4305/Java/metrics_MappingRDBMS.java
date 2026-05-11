





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRDBMS extends Mapping {

    private String dateFormat;
    private String timeFormat;
    private String user;
    private String password;
    private String dateTimeFormat;
    private String query;
    private String databaseType;



    public metrics_MappingRDBMS(
        String dateFormat,        String timeFormat,        String user,        String password,        String dateTimeFormat,        String query,        String databaseType    ) {
        super(
        );
        this.dateFormat = dateFormat;
        this.timeFormat = timeFormat;
        this.user = user;
        this.password = password;
        this.dateTimeFormat = dateTimeFormat;
        this.query = query;
        this.databaseType = databaseType;
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
    public String getDatetimeformat() {
        return dateTimeFormat;
    }

    public void setDatetimeformat(String dateTimeFormat) {
        this.dateTimeFormat = dateTimeFormat;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }
    public String getDatabasetype() {
        return databaseType;
    }

    public void setDatabasetype(String databaseType) {
        this.databaseType = databaseType;
    }


}