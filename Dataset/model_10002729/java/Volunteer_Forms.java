





import java.util.List;
import java.util.ArrayList;

public class Volunteer_Forms  {

    private int userID;
    private String userName;
    private String password;



    public Volunteer_Forms(
        int userID,        String userName,        String password    ) {
        this.userID = userID;
        this.userName = userName;
        this.password = password;
    }


    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
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


}