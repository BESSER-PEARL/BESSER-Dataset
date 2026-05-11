





import java.util.List;
import java.util.ArrayList;

public class application_OAuthAdmin  {

    private String username;
    private String passwordHash;



    public application_OAuthAdmin(
        String username,        String passwordHash    ) {
        this.username = username;
        this.passwordHash = passwordHash;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPasswordhash() {
        return passwordHash;
    }

    public void setPasswordhash(String passwordHash) {
        this.passwordHash = passwordHash;
    }


}