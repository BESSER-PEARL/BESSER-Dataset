





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String password;
    private String userName;
    private String lname;
    private String fname;





    private User user;


    public Registration(
        String password,        String userName,        String lname,        String fname    ) {
        this.password = password;
        this.userName = userName;
        this.lname = lname;
        this.fname = fname;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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