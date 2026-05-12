





import java.util.List;
import java.util.ArrayList;

public class sql_SqlProvides extends Provides {

    private String maxWait;
    private String timeBetweenEvictionRunsMillis;
    private String user;
    private String minIdle;
    private String metadata;
    private String maxIdle;
    private String storedProcedure;
    private String url;
    private String password;
    private String driver;
    private String maxActive;



    public sql_SqlProvides(
        String maxWait,        String timeBetweenEvictionRunsMillis,        String user,        String minIdle,        String metadata,        String maxIdle,        String storedProcedure,        String url,        String password,        String driver,        String maxActive    ) {
        super(
        );
        this.maxWait = maxWait;
        this.timeBetweenEvictionRunsMillis = timeBetweenEvictionRunsMillis;
        this.user = user;
        this.minIdle = minIdle;
        this.metadata = metadata;
        this.maxIdle = maxIdle;
        this.storedProcedure = storedProcedure;
        this.url = url;
        this.password = password;
        this.driver = driver;
        this.maxActive = maxActive;
    }


    public String getMaxwait() {
        return maxWait;
    }

    public void setMaxwait(String maxWait) {
        this.maxWait = maxWait;
    }
    public String getTimebetweenevictionrunsmillis() {
        return timeBetweenEvictionRunsMillis;
    }

    public void setTimebetweenevictionrunsmillis(String timeBetweenEvictionRunsMillis) {
        this.timeBetweenEvictionRunsMillis = timeBetweenEvictionRunsMillis;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getMinidle() {
        return minIdle;
    }

    public void setMinidle(String minIdle) {
        this.minIdle = minIdle;
    }
    public String getMetadata() {
        return metadata;
    }

    public void setMetadata(String metadata) {
        this.metadata = metadata;
    }
    public String getMaxidle() {
        return maxIdle;
    }

    public void setMaxidle(String maxIdle) {
        this.maxIdle = maxIdle;
    }
    public String getStoredprocedure() {
        return storedProcedure;
    }

    public void setStoredprocedure(String storedProcedure) {
        this.storedProcedure = storedProcedure;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getDriver() {
        return driver;
    }

    public void setDriver(String driver) {
        this.driver = driver;
    }
    public String getMaxactive() {
        return maxActive;
    }

    public void setMaxactive(String maxActive) {
        this.maxActive = maxActive;
    }


}