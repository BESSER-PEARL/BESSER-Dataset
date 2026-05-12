





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Shopping_Card  {

    private String Date_Added;
    private String Cart_ID;
    private String Produced_Id;
    private String Quantity;





    private online_shopping_Customer online_shopping_customer;




    private online_shopping_Customer online_shopping_customer;


    public online_shopping_Shopping_Card(
        String Date_Added,        String Cart_ID,        String Produced_Id,        String Quantity    ) {
        this.Date_Added = Date_Added;
        this.Cart_ID = Cart_ID;
        this.Produced_Id = Produced_Id;
        this.Quantity = Quantity;
    }


    public String getDate_added() {
        return Date_Added;
    }

    public void setDate_added(String Date_Added) {
        this.Date_Added = Date_Added;
    }
    public String getCart_id() {
        return Cart_ID;
    }

    public void setCart_id(String Cart_ID) {
        this.Cart_ID = Cart_ID;
    }
    public String getProduced_id() {
        return Produced_Id;
    }

    public void setProduced_id(String Produced_Id) {
        this.Produced_Id = Produced_Id;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }

    public online_shopping_Customer getOnline_shopping_customer() {
        return online_shopping_customer;
    }

    public void setOnline_shopping_customer(online_shopping_Customer online_shopping_customer) {
        this.online_shopping_customer = online_shopping_customer;
    }
    public online_shopping_Customer getOnline_shopping_customer() {
        return online_shopping_customer;
    }

    public void setOnline_shopping_customer(online_shopping_Customer online_shopping_customer) {
        this.online_shopping_customer = online_shopping_customer;
    }

}