





import java.util.List;
import java.util.ArrayList;

public class Web_User  {

    private String Username;
    private int Password;



    public Web_User(
        String Username,        int Password    ) {
        this.Username = Username;
        this.Password = Password;
    }


    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public int getPassword() {
        return Password;
    }

    public void setPassword(int Password) {
        this.Password = Password;
    }


}