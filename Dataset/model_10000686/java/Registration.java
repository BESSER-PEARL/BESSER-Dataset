





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String userName;
    private String password;
    private String lname;
    private String fname;





    private User user;


    public Registration(
        String userName,        String password,        String lname,        String fname    ) {
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}