





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Customer  {

    private String ID;
    private String Email;
    private String Address;
    private String Phone;





    private Online_Shopping_System_Web_User online_shopping_system_web_user;


    public Online_Shopping_System_Customer(
        String ID,        String Email,        String Address,        String Phone    ) {
        this.ID = ID;
        this.Email = Email;
        this.Address = Address;
        this.Phone = Phone;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }

    public Online_Shopping_System_Web_User getOnline_shopping_system_web_user() {
        return online_shopping_system_web_user;
    }

    public void setOnline_shopping_system_web_user(Online_Shopping_System_Web_User online_shopping_system_web_user) {
        this.online_shopping_system_web_user = online_shopping_system_web_user;
    }

}