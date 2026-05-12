





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Customer  {

    private int Age;
    private String Password;
    private String Address;
    private String Username;





    private Online_Shopping_Customer_points online_shopping_customer_points;




    private Online_Shopping_Item online_shopping_item;




    private Online_Shopping_Special_offers online_shopping_special_offers;


    public Online_Shopping_Customer(
        int Age,        String Password,        String Address,        String Username    ) {
        this.Age = Age;
        this.Password = Password;
        this.Address = Address;
        this.Username = Username;
    }


    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }

    public Online_Shopping_Customer_points getOnline_shopping_customer_points() {
        return online_shopping_customer_points;
    }

    public void setOnline_shopping_customer_points(Online_Shopping_Customer_points online_shopping_customer_points) {
        this.online_shopping_customer_points = online_shopping_customer_points;
    }
    public Online_Shopping_Item getOnline_shopping_item() {
        return online_shopping_item;
    }

    public void setOnline_shopping_item(Online_Shopping_Item online_shopping_item) {
        this.online_shopping_item = online_shopping_item;
    }
    public Online_Shopping_Special_offers getOnline_shopping_special_offers() {
        return online_shopping_special_offers;
    }

    public void setOnline_shopping_special_offers(Online_Shopping_Special_offers online_shopping_special_offers) {
        this.online_shopping_special_offers = online_shopping_special_offers;
    }

}