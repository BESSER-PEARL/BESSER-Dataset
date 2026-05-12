





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int Id;
    private String password;
    private String userName;
    private String userType;



    public User(
        int Id,        String password,        String userName,        String userType    ) {
        this.Id = Id;
        this.password = password;
        this.userName = userName;
        this.userType = userType;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
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
    public String getUsertype() {
        return userType;
    }

    public void setUsertype(String userType) {
        this.userType = userType;
    }


}