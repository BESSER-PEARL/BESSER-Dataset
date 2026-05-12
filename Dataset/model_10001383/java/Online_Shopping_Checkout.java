





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Checkout  {

    private String Billing_address;
    private String Checkout_address;
    private int Phone_number;
    private String Email_address;





    private Online_Shopping_PayPal_payment online_shopping_paypal_payment;




    private Online_Shopping_Card_payment online_shopping_card_payment;


    public Online_Shopping_Checkout(
        String Billing_address,        String Checkout_address,        int Phone_number,        String Email_address    ) {
        this.Billing_address = Billing_address;
        this.Checkout_address = Checkout_address;
        this.Phone_number = Phone_number;
        this.Email_address = Email_address;
    }


    public String getBilling_address() {
        return Billing_address;
    }

    public void setBilling_address(String Billing_address) {
        this.Billing_address = Billing_address;
    }
    public String getCheckout_address() {
        return Checkout_address;
    }

    public void setCheckout_address(String Checkout_address) {
        this.Checkout_address = Checkout_address;
    }
    public int getPhone_number() {
        return Phone_number;
    }

    public void setPhone_number(int Phone_number) {
        this.Phone_number = Phone_number;
    }
    public String getEmail_address() {
        return Email_address;
    }

    public void setEmail_address(String Email_address) {
        this.Email_address = Email_address;
    }

    public Online_Shopping_PayPal_payment getOnline_shopping_paypal_payment() {
        return online_shopping_paypal_payment;
    }

    public void setOnline_shopping_paypal_payment(Online_Shopping_PayPal_payment online_shopping_paypal_payment) {
        this.online_shopping_paypal_payment = online_shopping_paypal_payment;
    }
    public Online_Shopping_Card_payment getOnline_shopping_card_payment() {
        return online_shopping_card_payment;
    }

    public void setOnline_shopping_card_payment(Online_Shopping_Card_payment online_shopping_card_payment) {
        this.online_shopping_card_payment = online_shopping_card_payment;
    }

}