





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String userName;
    private String fname;
    private String lname;
    private String password;





    private User user;


    public Registration(
        String userName,        String fname,        String lname,        String password    ) {
        this.userName = userName;
        this.fname = fname;
        this.lname = lname;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}