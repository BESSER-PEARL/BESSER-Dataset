





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String UserId;
    private String login_status;
    private String password;



    public Login(
        String UserId,        String login_status,        String password    ) {
        this.UserId = UserId;
        this.login_status = login_status;
        this.password = password;
    }


    public String getUserid() {
        return UserId;
    }

    public void setUserid(String UserId) {
        this.UserId = UserId;
    }
    public String getLogin_status() {
        return login_status;
    }

    public void setLogin_status(String login_status) {
        this.login_status = login_status;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}