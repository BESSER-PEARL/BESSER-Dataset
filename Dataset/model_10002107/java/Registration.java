





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String userName;
    private None password;
    private String lname;
    private String fname;



    public Registration(
        String userName,        None password,        String lname,        String fname    ) {
        this.userName = userName;
        this.password = password;
        this.lname = lname;
        this.fname = fname;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public None getPassword() {
        return password;
    }

    public void setPassword(None password) {
        this.password = password;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }


}