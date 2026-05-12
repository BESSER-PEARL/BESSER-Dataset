





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String lname;
    private String userName;
    private None password;
    private String fname;





    private User user;


    public Registration(
        String lname,        String userName,        None password,        String fname    ) {
        this.lname = lname;
        this.userName = userName;
        this.password = password;
        this.fname = fname;
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}