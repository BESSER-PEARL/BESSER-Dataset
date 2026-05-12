





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Customer_Account  {

    private String Password;
    private String Username;





    private Online_Shopping_Item online_shopping_item;


    public Online_Shopping_Customer_Account(
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

    public Online_Shopping_Item getOnline_shopping_item() {
        return online_shopping_item;
    }

    public void setOnline_shopping_item(Online_Shopping_Item online_shopping_item) {
        this.online_shopping_item = online_shopping_item;
    }

}