





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Checkout  {

    private int Phone_Number;
    private String Billing_Address;
    private String Email_Address;
    private String Delivery_Address;





    private Online_Shopping_Card_Payment online_shopping_card_payment;




    private Online_Shopping_Paypal_Payment online_shopping_paypal_payment;


    public Online_Shopping_Checkout(
        int Phone_Number,        String Billing_Address,        String Email_Address,        String Delivery_Address    ) {
        this.Phone_Number = Phone_Number;
        this.Billing_Address = Billing_Address;
        this.Email_Address = Email_Address;
        this.Delivery_Address = Delivery_Address;
    }


    public int getPhone_number() {
        return Phone_Number;
    }

    public void setPhone_number(int Phone_Number) {
        this.Phone_Number = Phone_Number;
    }
    public String getBilling_address() {
        return Billing_Address;
    }

    public void setBilling_address(String Billing_Address) {
        this.Billing_Address = Billing_Address;
    }
    public String getEmail_address() {
        return Email_Address;
    }

    public void setEmail_address(String Email_Address) {
        this.Email_Address = Email_Address;
    }
    public String getDelivery_address() {
        return Delivery_Address;
    }

    public void setDelivery_address(String Delivery_Address) {
        this.Delivery_Address = Delivery_Address;
    }

    public Online_Shopping_Card_Payment getOnline_shopping_card_payment() {
        return online_shopping_card_payment;
    }

    public void setOnline_shopping_card_payment(Online_Shopping_Card_Payment online_shopping_card_payment) {
        this.online_shopping_card_payment = online_shopping_card_payment;
    }
    public Online_Shopping_Paypal_Payment getOnline_shopping_paypal_payment() {
        return online_shopping_paypal_payment;
    }

    public void setOnline_shopping_paypal_payment(Online_Shopping_Paypal_Payment online_shopping_paypal_payment) {
        this.online_shopping_paypal_payment = online_shopping_paypal_payment;
    }

}