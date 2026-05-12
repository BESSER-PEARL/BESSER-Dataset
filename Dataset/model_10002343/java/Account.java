





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private int Password;
    private String Username;



    public Account(
        int Password,        String Username    ) {
        this.Password = Password;
        this.Username = Username;
    }


    public int getPassword() {
        return Password;
    }

    public void setPassword(int Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }


}