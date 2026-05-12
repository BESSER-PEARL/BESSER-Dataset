





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Shopping_Cart  {

    private String created;





    private Online_Shopping_System_Web_User online_shopping_system_web_user;


    public Online_Shopping_System_Shopping_Cart(
        String created    ) {
        this.created = created;
    }


    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }

    public Online_Shopping_System_Web_User getOnline_shopping_system_web_user() {
        return online_shopping_system_web_user;
    }

    public void setOnline_shopping_system_web_user(Online_Shopping_System_Web_User online_shopping_system_web_user) {
        this.online_shopping_system_web_user = online_shopping_system_web_user;
    }

}