





import java.util.List;
import java.util.ArrayList;

public class End_User  {

    private String login;
    private String password;
    private String userType;





    private Internet_Users internet_users;




    private Thick_Client_Users thick_client_users;


    public End_User(
        String login,        String password,        String userType    ) {
        this.login = login;
        this.password = password;
        this.userType = userType;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsertype() {
        return userType;
    }

    public void setUsertype(String userType) {
        this.userType = userType;
    }

    public Internet_Users getInternet_users() {
        return internet_users;
    }

    public void setInternet_users(Internet_Users internet_users) {
        this.internet_users = internet_users;
    }
    public Thick_Client_Users getThick_client_users() {
        return thick_client_users;
    }

    public void setThick_client_users(Thick_Client_Users thick_client_users) {
        this.thick_client_users = thick_client_users;
    }

}