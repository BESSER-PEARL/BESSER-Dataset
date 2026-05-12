





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Password;
    private String loginStatus;
    private String User_Id;





    private Client client;


    public User(
        String Password,        String loginStatus,        String User_Id    ) {
        this.Password = Password;
        this.loginStatus = loginStatus;
        this.User_Id = User_Id;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getLoginstatus() {
        return loginStatus;
    }

    public void setLoginstatus(String loginStatus) {
        this.loginStatus = loginStatus;
    }
    public String getUser_id() {
        return User_Id;
    }

    public void setUser_id(String User_Id) {
        this.User_Id = User_Id;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

}