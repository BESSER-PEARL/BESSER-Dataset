





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Order  {

    private int Placed_Date;
    private None Contents;
    private String State;





    private Online_Shopping_Card_payment online_shopping_card_payment;




    private Online_Shopping_PayPal_payment online_shopping_paypal_payment;


    public Online_Shopping_Order(
        int Placed_Date,        None Contents,        String State    ) {
        this.Placed_Date = Placed_Date;
        this.Contents = Contents;
        this.State = State;
    }


    public int getPlaced_date() {
        return Placed_Date;
    }

    public void setPlaced_date(int Placed_Date) {
        this.Placed_Date = Placed_Date;
    }
    public None getContents() {
        return Contents;
    }

    public void setContents(None Contents) {
        this.Contents = Contents;
    }
    public String getState() {
        return State;
    }

    public void setState(String State) {
        this.State = State;
    }

    public Online_Shopping_Card_payment getOnline_shopping_card_payment() {
        return online_shopping_card_payment;
    }

    public void setOnline_shopping_card_payment(Online_Shopping_Card_payment online_shopping_card_payment) {
        this.online_shopping_card_payment = online_shopping_card_payment;
    }
    public Online_Shopping_PayPal_payment getOnline_shopping_paypal_payment() {
        return online_shopping_paypal_payment;
    }

    public void setOnline_shopping_paypal_payment(Online_Shopping_PayPal_payment online_shopping_paypal_payment) {
        this.online_shopping_paypal_payment = online_shopping_paypal_payment;
    }

}