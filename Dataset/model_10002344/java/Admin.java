





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String password;
    private String userName;
    private int userID;



    public Admin(
        String password,        String userName,        int userID    ) {
        this.password = password;
        this.userName = userName;
        this.userID = userID;
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
    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
        this.userID = userID;
    }


}