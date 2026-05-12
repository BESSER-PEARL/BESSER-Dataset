





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String lname;
    private String username;
    private String fname;



    public User(
        String lname,        String username,        String fname    ) {
        this.lname = lname;
        this.username = username;
        this.fname = fname;
    }


    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }


}