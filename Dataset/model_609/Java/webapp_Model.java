





import java.util.List;
import java.util.ArrayList;

public class webapp_Model  {

    private String userName;
    private String url;
    private String password;
    private String databaseName;





    private webapp_WebApp webapp_webapp;


    public webapp_Model(
        String userName,        String url,        String password,        String databaseName    ) {
        this.userName = userName;
        this.url = url;
        this.password = password;
        this.databaseName = databaseName;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
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
    public String getDatabasename() {
        return databaseName;
    }

    public void setDatabasename(String databaseName) {
        this.databaseName = databaseName;
    }

    public webapp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(webapp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }

}