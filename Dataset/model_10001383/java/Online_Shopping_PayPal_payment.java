





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_PayPal_payment  {

    private String Password;
    private String Username;
    private String attribute;



    public Online_Shopping_PayPal_payment(
        String Password,        String Username,        String attribute    ) {
        this.Password = Password;
        this.Username = Username;
        this.attribute = attribute;
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
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}