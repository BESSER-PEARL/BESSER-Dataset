





import java.util.List;
import java.util.ArrayList;

public class Models_User  {

    private String UserId;
    private String password;
    private String email;



    public Models_User(
        String UserId,        String password,        String email    ) {
        this.UserId = UserId;
        this.password = password;
        this.email = email;
    }


    public String getUserid() {
        return UserId;
    }

    public void setUserid(String UserId) {
        this.UserId = UserId;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}