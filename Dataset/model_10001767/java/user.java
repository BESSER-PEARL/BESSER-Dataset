





import java.util.List;
import java.util.ArrayList;

public class user  {

    private String email;
    private String loginstatus;
    private String password;
    private int UserId;



    public user(
        String email,        String loginstatus,        String password,        int UserId    ) {
        this.email = email;
        this.loginstatus = loginstatus;
        this.password = password;
        this.UserId = UserId;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLoginstatus() {
        return loginstatus;
    }

    public void setLoginstatus(String loginstatus) {
        this.loginstatus = loginstatus;
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


}