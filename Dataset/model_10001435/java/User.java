





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int UserId;
    private String Password;



    public User(
        int UserId,        String Password    ) {
        this.UserId = UserId;
        this.Password = Password;
    }


    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}