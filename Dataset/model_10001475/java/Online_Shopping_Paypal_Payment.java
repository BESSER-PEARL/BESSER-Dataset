





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Paypal_Payment  {

    private String Password;
    private String Username;



    public Online_Shopping_Paypal_Payment(
        String Password,        String Username    ) {
        this.Password = Password;
        this.Username = Username;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }


}