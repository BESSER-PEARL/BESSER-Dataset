





import java.util.List;
import java.util.ArrayList;

public class Volunteer  {

    private String userName;
    private String password;
    private int userID;



    public Volunteer(
        String userName,        String password,        int userID    ) {
        this.userName = userName;
        this.password = password;
        this.userID = userID;
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
    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
        this.userID = userID;
    }


}