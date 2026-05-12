





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private int UserId;
    private String UserName;



    public Login(
        int UserId,        String UserName    ) {
        this.UserId = UserId;
        this.UserName = UserName;
    }


    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }


}