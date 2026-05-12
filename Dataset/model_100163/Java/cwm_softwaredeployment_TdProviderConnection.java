





import java.util.List;
import java.util.ArrayList;

public class cwm_softwaredeployment_TdProviderConnection extends ProviderConnection {

    private String password;
    private String connectionString;
    private String login;
    private String driverClassName;



    public cwm_softwaredeployment_TdProviderConnection(
        String password,        String connectionString,        String login,        String driverClassName    ) {
        super(
        );
        this.password = password;
        this.connectionString = connectionString;
        this.login = login;
        this.driverClassName = driverClassName;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getConnectionstring() {
        return connectionString;
    }

    public void setConnectionstring(String connectionString) {
        this.connectionString = connectionString;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getDriverclassname() {
        return driverClassName;
    }

    public void setDriverclassname(String driverClassName) {
        this.driverClassName = driverClassName;
    }


}