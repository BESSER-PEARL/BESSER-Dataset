





import java.util.List;
import java.util.ArrayList;

public class Sign_Up  {

    private None password;
    private String fname;
    private String userName;
    private String lname;



    public Sign_Up(
        None password,        String fname,        String userName,        String lname    ) {
        this.password = password;
        this.fname = fname;
        this.userName = userName;
        this.lname = lname;
    }


    public None getPassword() {
        return password;
    }

    public void setPassword(None password) {
        this.password = password;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }


}