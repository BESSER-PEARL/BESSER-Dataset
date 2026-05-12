





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String fname;
    private String username;
    private String lname;
    private String password;



    public User(
        String fname,        String username,        String lname,        String password    ) {
        this.fname = fname;
        this.username = username;
        this.lname = lname;
        this.password = password;
    }


    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}