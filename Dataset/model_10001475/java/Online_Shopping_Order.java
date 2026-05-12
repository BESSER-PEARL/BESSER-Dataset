





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Order  {

    private None Contents;
    private String Placed_Date;





    private Online_Shopping_Order_Item online_shopping_order_item;




    private Online_Shopping_Paypal_Payment online_shopping_paypal_payment;




    private Online_Shopping_Card_Payment online_shopping_card_payment;


    public Online_Shopping_Order(
        None Contents,        String Placed_Date    ) {
        this.Contents = Contents;
        this.Placed_Date = Placed_Date;
    }


    public None getContents() {
        return Contents;
    }

    public void setContents(None Contents) {
        this.Contents = Contents;
    }
    public String getPlaced_date() {
        return Placed_Date;
    }

    public void setPlaced_date(String Placed_Date) {
        this.Placed_Date = Placed_Date;
    }

    public Online_Shopping_Order_Item getOnline_shopping_order_item() {
        return online_shopping_order_item;
    }

    public void setOnline_shopping_order_item(Online_Shopping_Order_Item online_shopping_order_item) {
        this.online_shopping_order_item = online_shopping_order_item;
    }
    public Online_Shopping_Paypal_Payment getOnline_shopping_paypal_payment() {
        return online_shopping_paypal_payment;
    }

    public void setOnline_shopping_paypal_payment(Online_Shopping_Paypal_Payment online_shopping_paypal_payment) {
        this.online_shopping_paypal_payment = online_shopping_paypal_payment;
    }
    public Online_Shopping_Card_Payment getOnline_shopping_card_payment() {
        return online_shopping_card_payment;
    }

    public void setOnline_shopping_card_payment(Online_Shopping_Card_Payment online_shopping_card_payment) {
        this.online_shopping_card_payment = online_shopping_card_payment;
    }

}