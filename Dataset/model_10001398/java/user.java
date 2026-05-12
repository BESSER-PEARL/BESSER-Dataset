





import java.util.List;
import java.util.ArrayList;

public class user  {

    private String password;
    private int UserId;
    private String loginstatus;
    private String email;



    public user(
        String password,        int UserId,        String loginstatus,        String email    ) {
        this.password = password;
        this.UserId = UserId;
        this.loginstatus = loginstatus;
        this.email = email;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }
    public String getLoginstatus() {
        return loginstatus;
    }

    public void setLoginstatus(String loginstatus) {
        this.loginstatus = loginstatus;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}