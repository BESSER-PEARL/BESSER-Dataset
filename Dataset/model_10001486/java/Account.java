





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String UserName;
    private String Info;



    public Account(
        String UserName,        String Info    ) {
        this.UserName = UserName;
        this.Info = Info;
    }


    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getInfo() {
        return Info;
    }

    public void setInfo(String Info) {
        this.Info = Info;
    }


}