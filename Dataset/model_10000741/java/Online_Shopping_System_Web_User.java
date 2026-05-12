





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Web_User  {

    private String passwd;
    private String login_id;





    private Online_Shopping_System_Shopping_Cart online_shopping_system_shopping_cart;


    public Online_Shopping_System_Web_User(
        String passwd,        String login_id    ) {
        this.passwd = passwd;
        this.login_id = login_id;
    }


    public String getPasswd() {
        return passwd;
    }

    public void setPasswd(String passwd) {
        this.passwd = passwd;
    }
    public String getLogin_id() {
        return login_id;
    }

    public void setLogin_id(String login_id) {
        this.login_id = login_id;
    }

    public Online_Shopping_System_Shopping_Cart getOnline_shopping_system_shopping_cart() {
        return online_shopping_system_shopping_cart;
    }

    public void setOnline_shopping_system_shopping_cart(Online_Shopping_System_Shopping_Cart online_shopping_system_shopping_cart) {
        this.online_shopping_system_shopping_cart = online_shopping_system_shopping_cart;
    }

}