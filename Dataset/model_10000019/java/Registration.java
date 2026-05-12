





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String lname;
    private String fname;
    private None password;
    private String userName;





    private User user;


    public Registration(
        String lname,        String fname,        None password,        String userName    ) {
        this.lname = lname;
        this.fname = fname;
        this.password = password;
        this.userName = userName;
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}