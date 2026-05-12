





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String lname;
    private String userName;
    private String fname;
    private None password;





    private User user;


    public Registration(
        String lname,        String userName,        String fname,        None password    ) {
        this.lname = lname;
        this.userName = userName;
        this.fname = fname;
        this.password = password;
    }


    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public None getPassword() {
        return password;
    }

    public void setPassword(None password) {
        this.password = password;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}