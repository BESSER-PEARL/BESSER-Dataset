





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String fname;
    private String userName;
    private None password;
    private String lname;





    private User user;


    public Registration(
        String fname,        String userName,        None password,        String lname    ) {
        this.fname = fname;
        this.userName = userName;
        this.password = password;
        this.lname = lname;
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}