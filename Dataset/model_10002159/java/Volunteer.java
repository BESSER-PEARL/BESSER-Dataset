





import java.util.List;
import java.util.ArrayList;

public class Volunteer  {

    private String userName;
    private int userID;
    private String password;



    public Volunteer(
        String userName,        int userID,        String password    ) {
        this.userName = userName;
        this.userID = userID;
        this.password = password;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
        this.userID = userID;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}