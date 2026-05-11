





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRDBMS extends Mapping {

    private String databaseType;
    private String query;
    private String dateTimeFormat;
    private String dateFormat;
    private String password;
    private String user;
    private String timeFormat;



    public metrics_MappingRDBMS(
        String databaseType,        String query,        String dateTimeFormat,        String dateFormat,        String password,        String user,        String timeFormat    ) {
        super(
        );
        this.databaseType = databaseType;
        this.query = query;
        this.dateTimeFormat = dateTimeFormat;
        this.dateFormat = dateFormat;
        this.password = password;
        this.user = user;
        this.timeFormat = timeFormat;
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
    public String getDatetimeformat() {
        return dateTimeFormat;
    }

    public void setDatetimeformat(String dateTimeFormat) {
        this.dateTimeFormat = dateTimeFormat;
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
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getTimeformat() {
        return timeFormat;
    }

    public void setTimeformat(String timeFormat) {
        this.timeFormat = timeFormat;
    }


}