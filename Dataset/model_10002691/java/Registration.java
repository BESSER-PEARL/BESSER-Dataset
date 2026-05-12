





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private None password;
    private String userName;
    private String fname;
    private String lname;





    private User user;


    public Registration(
        None password,        String userName,        String fname,        String lname    ) {
        this.password = password;
        this.userName = userName;
        this.fname = fname;
        this.lname = lname;
    }


    public None getPassword() {
        return password;
    }

    public void setPassword(None password) {
        this.password = password;
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