





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private int password;
    private String username;



    public Login(
        int password,        String username    ) {
        this.password = password;
        this.username = username;
    }


    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}